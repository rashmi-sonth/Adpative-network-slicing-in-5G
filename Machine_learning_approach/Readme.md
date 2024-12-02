# Machine Learning Approach for 5G Network Slicing

This project applies machine learning models to analyze and optimize resource allocation in 5G network slicing. It includes data preprocessing, training, and evaluation of various machine learning models, and visualizes the performance metrics.

---

## 📂 Folder Structure

```plaintext
Machine_learning_approach/
├── Dataset/
│   ├── 5G Dataset NS.csv       # Dataset containing 5G network slicing features and labels.
├── heatmap.png                 # Visualization of model performance metrics.
├── ML_approaches.ipynb         # Jupyter notebook with code for machine learning implementation.
```

---

## 📄 Files Description

### **1. Dataset/5G Dataset NS.csv**
This CSV file contains the dataset used for training and testing the machine learning models. It includes features such as:

- **UserDeviceType**: Device type of the user (e.g., Smartphone, IoT, etc.).
- **Duration(sec)**: Session duration in seconds.
- **PacketLossRate**: Reliability measure of packets lost.
- **Latency**: Packet delay budget in milliseconds.
- **Bandwidth**: Bandwidth consumption in GHz.
- **DelayRate**: Delay rate in Mbps.
- **Speed**: Connection speed in Mbps.
- **Jitter**: Variation in packet delay in picoseconds.
- **ModulationType**: Modulation technique used.
- **SliceType**: Label representing the slice category (e.g., eMBB, mMTC, uRLLC).

---

### **2. heatmap.png**
A heatmap visualizing the performance metrics (Accuracy, Precision, Recall, F1-Score) of various machine learning models. Models compared include:

- Random Forest
- Gradient Boosting
- AdaBoost
- Stacking Classifier
- Voting Classifier, and more.

This visualization helps in identifying the best-performing models for 5G network slicing tasks.

---

### **3. ML_approaches.ipynb**
This Jupyter Notebook contains the following:
- **Data Preprocessing**:
  - Handles missing values and encodes categorical features using `LabelEncoder`.
  - Splits data into training and testing sets.
- **Model Training**:
  - Implements supervised learning algorithms like Random Forest, AdaBoost, Gradient Boosting, and Stacking Classifier.
  - Fine-tunes hyperparameters using `GridSearchCV`.
- **Performance Evaluation**:
  - Evaluates models using metrics like Accuracy, Precision, Recall, and F1-Score.
  - Generates a confusion matrix and heatmap for better visualization.

---

## 🚀 How to Run the Notebook

### Prerequisites
1. **Python 3.9+** installed.
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

### Steps
1. Navigate to the project directory:
   ```bash
   cd Machine_learning_approach
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook ML_approaches.ipynb
   ```
3. Run all cells in the notebook to preprocess the data, train models, and evaluate results.

---

## 🔑 Key Features

1. **Comprehensive Dataset**:
   - Real-world dataset simulating diverse 5G network scenarios.
2. **Model Evaluation**:
   - Comparative analysis of machine learning algorithms for efficient slice management.
3. **Visualization**:
   - Heatmap and confusion matrix for performance evaluation.
4. **Automation**:
   - Automates hyperparameter tuning for better accuracy and reliability.

---

## 📝 Example Workflow

1. Load the dataset from `Dataset/5G Dataset NS.csv`.
2. Preprocess the data:
   - Handle missing values and encode categorical data.
3. Train and evaluate models:
   - Compare multiple supervised learning models for classification of `SliceType`.
4. Visualize results:
   - Generate a heatmap of metrics for all models.

---

## 📊 Outputs

### **Performance Heatmap**:
`heatmap.png` provides an intuitive visualization of model metrics (Accuracy, Precision, Recall, F1-Score).

### **Best Model**:
The `Stacking Classifier` emerges as the top-performing model, achieving the highest scores across evaluation metrics.

---

## 📩 Contact

For any queries or contributions, feel free to reach out to the project maintainer @rashmi.sonth@sjsu.edu
