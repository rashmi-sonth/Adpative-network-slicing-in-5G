# Traditional Approach for 5G Network Slicing

This project simulates and analyzes 5G network slicing using traditional resource allocation algorithms. It generates visual and textual outputs based on network configurations provided as input files.

---

## 📂 Directory Structure

```plaintext
Traditional_approach/
├── code/
│   ├── __init__.py
│   ├── __main__.py
│   ├── BaseStation.py
│   ├── Client.py
│   ├── Container.py
│   ├── Coverage.py
│   ├── Distributor.py
│   ├── Graph.py
│   ├── Slice.py
│   ├── Stats.py
│   └── utils.py
├── Input/
│   ├── network1.yml
│   ├── network2.yml
├── output/
│   ├── network1.png
│   ├── network1.txt
│   ├── network2.png
│   └── network2.txt
```

---

## 📥 Input Files

The **Input** folder contains YAML configuration files defining network scenarios. Each file specifies:

- **Base Station Information**: Locations, coverage radii, and capacity constraints.
- **Client Mobility**: Patterns and resource consumption behaviors.
- **Resource Allocation Rules**: Policies for distributing bandwidth and managing slices.

### Input Examples:
- **`network1.yml`**: Represents scenario 1 with specific base station and client configurations.
- **`network2.yml`**: Represents scenario 2 with a different network setup.

---

## 📤 Output Files

Simulation results are stored in the **output** folder and include:

1. **Graphical Output (`.png`)**: Visual representation of base station coverage, client distribution, and slice utilization.
2. **Logs (`.txt`)**: Detailed network statistics, including:
   - Total bandwidth usage
   - Connected/disconnected client ratios
   - Resource allocation efficiency per slice

### Output Examples:
- `network1.png` / `network1.txt`
- `network2.png` / `network2.txt`

---

## 🚀 Running the Simulation

### Steps:

1. **Navigate to the project directory**:
   ```bash
   cd Traditional_approach
   ```

2. **Run the simulation**:
   ```bash
   python3 -m code Input/<input_file>.yml
   ```
   Replace `<input_file>` with the desired YAML configuration file.

### Example Command:
To run `network2.yml`:
```bash
python3 -m code Input/network2.yml
```

---

## 🛠️ Prerequisites

Ensure the following setup:

1. **Python Version**: Python 3.9 or higher.
2. **Required Libraries**:
   - `pyyaml`
   - `simpy`
   - `matplotlib`
   - `numpy`

Install dependencies:
```bash
pip install pyyaml simpy matplotlib numpy
```

---

## 🔑 Key Features

- **Dynamic Resource Allocation**:
  - Implements priority-based and dynamic allocation strategies for network slices.
- **Real-Time Visualization**:
  - Outputs client connections and base station interactions in a graphical format.
- **Comprehensive Statistics**:
  - Logs detailed metrics like bandwidth utilization, client connection ratios, and slice performance.

---

## 📝 Example Workflow

1. **Input Preparation**:
   - Place YAML configuration files in the `Input` folder.
   - Ensure accurate specifications for base stations, clients, and slices.

2. **Run Simulation**:
   ```bash
   python3 -m code Input/network1.yml
   ```

3. **View Results**:
   - Open the generated `.png` file in the `output` folder for a visual overview.
   - Review the corresponding `.txt` file for detailed statistics.

---

## 📊 Example Commands

- Run the simulation for `network1.yml`:
  ```bash
  python3 -m code Input/network1.yml
  ```

- Check visual and textual output:
  - Open `output/network1.png` for graphical results.
  - Inspect `output/network1.txt` for detailed metrics.

---

## 📈 Example Outputs

### Visual Output:
![Example Network Graph](output/network1.png)

### Log Output (`network1.txt`):
```plaintext
Total Bandwidth Usage: 1.2 Gbps
Connected Clients Ratio: 85%
Bandwidth Utilization Efficiency: 92%
...
```

---

## 🤝 Contact

For any queries, issues, or contributions, reach out to the project maintainer @rashmi.sonth@sjsu.edu

