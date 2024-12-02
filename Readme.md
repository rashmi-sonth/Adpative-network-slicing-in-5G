# 5G Network Slicing: Comparative Approaches

This repository explores two distinct approaches to address resource allocation and Quality of Service (QoS) challenges in 5G network slicing:
1. **Traditional Approach**: Employing established algorithms for deterministic resource management.
2. **Machine Learning Approach**: Leveraging supervised learning and ensemble models to predict slice requirements and optimize resource utilization.

The project focuses on the comparative analysis of these methodologies, highlighting their implementations and performance evaluations.

---

## 📂 Folder Structure

```plaintext
5G_Network_Slicing/
├── Machine_learning_approach/    # ML-based solution for resource allocation.
│   ├── Dataset/                  # Contains the 5G dataset for ML modeling.
│   ├── heatmap.png               # Visualization of ML model metrics.
│   └── ML_approaches.ipynb       # Jupyter Notebook implementing ML models.
│
└── Traditional_approach/         # Traditional algorithm-based solution.
    ├── code/                     # Python scripts for resource allocation.
    ├── Input/                    # Input YAML files defining network scenarios.
    └── output/                   # Simulation results: visualizations and logs.
```

Each sub-folder contains its own `README.md` file that explains the implementation details, usage, and outputs for that specific approach.

---

## 📘 Overview of Approaches

### **1. Traditional Approach**
- **Objective**: Allocate resources using deterministic algorithms.
- **Key Features**:
  - **Dynamic Allocation**: Adjusts resources in real-time based on demand.
  - **Priority-Based Allocation**: Ensures resources are directed to critical applications.

### **2. Machine Learning Approach**
- **Objective**: Predict slice requirements and optimize resource allocation.
- **Key Features**:
  - Implements models such as Random Forest, Gradient Boosting, and Stacking Classifier.
  - Evaluates performance using metrics like Accuracy, Precision, Recall, and F1-Score.
  - Heatmaps visualize model performance.

---

## 🔑 Key Highlights

1. **Comprehensive Comparison**:
   - Evaluates the strengths and limitations of traditional algorithms and machine learning approaches.
2. **Realistic Simulations**:
   - Uses a representative 5G dataset and practical configurations for network slicing.
3. **Scalability**:
   - Frameworks adaptable to evolving challenges in 5G and beyond.

---

## 📩 Contact

For further inquiries, issues, or collaborations, refer to the `README.md` files within each sub-folder for more details.
