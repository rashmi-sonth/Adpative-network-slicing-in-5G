import math
import os
import random
import sys
import time
import simpy
import yaml
import logging

from .BaseStation import BaseStation
from .Client import Client
from .Coverage import Coverage
from .Distributor import Distributor
from .Graph import Graph
from .Slice import Slice
from .Stats import Stats

from .utils import KDTree

# Helper function to map distribution names to Python's random module functions
def get_dist(d):
    """
    Maps a distribution name to a corresponding random function.

    Args:
        d (str): Name of the distribution.

    Returns:
        function: Corresponding random function from the Python random module.
    """
    return {
        'randrange': random.randrange,  # start, stop, step
        'randint': random.randint,      # a, b
        'random': random.random,
        'uniform': random.uniform,     # a, b
        'triangular': random.triangular,  # low, high, mode
        'beta': random.betavariate,    # alpha, beta
        'expo': random.expovariate,    # lambda
        'gamma': random.gammavariate,  # alpha, beta
        'gauss': random.gauss,         # mu, sigma
        'lognorm': random.lognormvariate,  # mu, sigma
        'normal': random.normalvariate,    # mu, sigma
        'vonmises': random.vonmisesvariate,  # mu, kappa
        'pareto': random.paretovariate,    # alpha
        'weibull': random.weibullvariate   # alpha, beta
    }.get(d)

def get_random_mobility_pattern(vals, mobility_patterns):
    """
    Selects a random mobility pattern based on cumulative weights.

    Args:
        vals (list): Cumulative weights for mobility patterns.
        mobility_patterns (list): List of mobility pattern objects.

    Returns:
        object: Selected mobility pattern.
    """
    i = 0
    r = random.random()  # Generate a random value between 0 and 1
    while vals[i] < r:   # Increment until the cumulative weight is exceeded
        i += 1
    return mobility_patterns[i]

def get_random_slice_index(vals):
    """
    Selects a random slice index based on cumulative weights.

    Args:
        vals (list): Cumulative weights for slices.

    Returns:
        int: Selected slice index.
    """
    i = 0
    r = random.random()  # Generate a random value between 0 and 1
    while vals[i] < r:   # Increment until the cumulative weight is exceeded
        i += 1
    return i

# Setup logging to log to both terminal and file
def setup_logging(log_file):
    """
    Configure logging to send logs to both the terminal and a file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # Logs to the terminal
            logging.FileHandler(log_file, mode="w")  # Logs to a file
        ]
    )

# Load the configuration file in YAML format
CONF_FILENAME = os.path.join(os.path.dirname(__file__), sys.argv[1])
try:
    with open(CONF_FILENAME, 'r') as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)  # Parse YAML
except FileNotFoundError:
    logging.error('File Not Found: %s', CONF_FILENAME)
    exit(0)

# Initialize the random seed and simulation environment
random.seed()
env = simpy.Environment()

SETTINGS = data['settings']
SLICES_INFO = data['slices']
NUM_CLIENTS = SETTINGS['num_clients']
MOBILITY_PATTERNS = data['mobility_patterns']
BASE_STATIONS = data['base_stations']
CLIENTS = data['clients']

SETTINGS['log_file'] = os.path.join(os.getcwd(), 'output', SETTINGS['log_file'])
setup_logging(SETTINGS['log_file'])
print("Log file path:", SETTINGS['log_file'])

logging.info("Configuration loaded successfully.")

# Prepare cumulative weights for slices and mobility patterns
collected, slice_weights = 0, []
for _, s in SLICES_INFO.items():
    collected += s['client_weight']
    slice_weights.append(collected)

collected, mb_weights = 0, []
for _, mb in MOBILITY_PATTERNS.items():
    collected += mb['client_weight']
    mb_weights.append(collected)

logging.info("Cumulative weights for slices and mobility patterns calculated.")

# Initialize mobility and usage patterns
mobility_patterns = []
for name, mb in MOBILITY_PATTERNS.items():
    mobility_pattern = Distributor(name, get_dist(mb['distribution']), *mb['params'])
    mobility_patterns.append(mobility_pattern)

usage_patterns = {}
for name, s in SLICES_INFO.items():
    usage_patterns[name] = Distributor(name, get_dist(s['usage_pattern']['distribution']), *s['usage_pattern']['params'])

# Initialize base stations and their slices
base_stations = []
for i, b in enumerate(BASE_STATIONS):
    slices = []
    capacity = b['capacity_bandwidth']
    for name, s in SLICES_INFO.items():
        s_cap = capacity * b['ratios'][name]
        s = Slice(name, b['ratios'][name], 0, s['client_weight'],
                  s['delay_tolerance'], s['qos_class'],
                  s['bandwidth_guaranteed'], s['bandwidth_max'],
                  s_cap, usage_patterns[name])
        s.capacity = simpy.Container(env, init=s_cap, capacity=s_cap)
        slices.append(s)
    base_station = BaseStation(i, Coverage((b['x'], b['y']), b['coverage']), capacity, slices)
    base_stations.append(base_station)

logging.info("Base stations initialized.")

# Initialize clients with random locations and mobility patterns
ufp = CLIENTS['usage_frequency']
usage_freq_pattern = Distributor('ufp', get_dist(ufp['distribution']), *ufp['params'], divide_scale=ufp['divide_scale'])

x_vals = SETTINGS['statistics_params']['x']
y_vals = SETTINGS['statistics_params']['y']
stats = Stats(env, base_stations, None, ((x_vals['min'], x_vals['max']), (y_vals['min'], y_vals['max'])))

clients = []
for i in range(NUM_CLIENTS):
    loc_x = CLIENTS['location']['x']
    loc_y = CLIENTS['location']['y']
    location_x = get_dist(loc_x['distribution'])(*loc_x['params'])
    location_y = get_dist(loc_y['distribution'])(*loc_y['params'])

    mobility_pattern = get_random_mobility_pattern(mb_weights, mobility_patterns)
    connected_slice_index = get_random_slice_index(slice_weights)
    c = Client(i, env, location_x, location_y,
               mobility_pattern, usage_freq_pattern.generate_scaled(), connected_slice_index, stats)
    clients.append(c)

logging.info("Clients initialized and assigned to mobility patterns.")

# Assign clients to base stations using KDTree for optimization
KDTree.limit = SETTINGS['limit_closest_base_stations']
KDTree.run(clients, base_stations, 0)

# Start collecting statistics and run the simulation
stats.clients = clients
env.process(stats.collect())
logging.info("Simulation started.")
env.run(until=int(SETTINGS['simulation_time']))
logging.info("Simulation completed.")

# Print statistics for each client
for client in clients:
    logging.info(client)
    logging.info(f'\tTotal connected time: {client.total_connected_time:>5}')
    logging.info(f'\tTotal unconnected time: {client.total_unconnected_time:>5}')
    logging.info(f'\tTotal request count: {client.total_request_count:>5}')
    logging.info(f'\tTotal consume time: {client.total_consume_time:>5}')
    logging.info(f'\tTotal usage: {client.total_usage:>5}')
logging.info(stats.get_stats())

# Plot results if plotting is enabled
if SETTINGS['plotting_params']['plotting']:
    xlim_left = int(SETTINGS['simulation_time'] * SETTINGS['statistics_params']['warmup_ratio'])
    xlim_right = int(SETTINGS['simulation_time'] * (1 - SETTINGS['statistics_params']['cooldown_ratio'])) + 1

    SETTINGS['plotting_params']['plot_file'] = os.path.join(os.getcwd(), 'output', SETTINGS['plotting_params']['plot_file'])
    
    graph = Graph(base_stations, clients, (xlim_left, xlim_right),
                  ((x_vals['min'], x_vals['max']), (y_vals['min'], y_vals['max'])),
                  output_dpi=SETTINGS['plotting_params']['plot_file_dpi'],
                  scatter_size=SETTINGS['plotting_params']['scatter_size'],
                  output_filename=SETTINGS['plotting_params']['plot_file'])
    graph.draw_all(*stats.get_stats())
    if SETTINGS['plotting_params']['plot_save']:
        graph.save_fig()
    if SETTINGS['plotting_params']['plot_show']:
        graph.show_plot()

logging.info('Simulation completed. Results saved to: %s', SETTINGS['plotting_params']['plot_file'])
