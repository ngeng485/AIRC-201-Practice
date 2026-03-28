import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Ensure results directory exists relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Load data
data_path = os.path.join(script_dir, "..", "data", "fraud_transactions.csv")
df = pd.read_csv(data_path)

# ---------------------------------------------------------
# FRAUD DETECTION PIPELINE
# ---------------------------------------------------------

# START STUDENT IMPLEMENTATION HERE

# Step 1: Preprocessing
# TODO: Inspect the dataframe. Drop irrelevant columns like 'nameOrig' and 'nameDest' 
#       which are arbitrary string IDs. 
# TODO: Encode categorical variables. You may want to use `pd.get_dummies` or `LabelEncoder` 
#       for the 'type' column.
# TODO: Separate features (X) and labels (y). The target label is 'isFraud'.
# TODO: Scale numerical features using `StandardScaler` so that models like Ridge converge easily.

# Step 2: Train/Test Split
# TODO: Split the data into training and testing sets with an 80/20 split.
#       Ensure you set a random state (e.g., random_state=42) for reproducibility and shuffle the data.

# Step 3: Train Three Models
# TODO: Train three models of your choice. If you are undecided, try the following classification models:
#       1. Ridge Classifier (from sklearn.linear_model)
#          - Suggested Hyperparameters: alpha=1.0 or 10.0, solver='auto'
#       2. Random Forest (from sklearn.ensemble)
#          - Suggested Hyperparameters: n_estimators=100, max_depth=10, random_state=42
#       3. AdaBoost (from sklearn.ensemble)
#          - Suggested Hyperparameters: n_estimators=50, learning_rate=1.0, random_state=42

# Step 4: Evaluate Models
# TODO: For each model, generate predictions on BOTH the training and test sets.
# TODO: Calculate and report Accuracy, False Positive Rate (FPR), False Negative Rate (FNR), 
#       True Positive Rate (TPR), and True Negative Rate (TNR) for each evaluation.
#       (3 models x 2 sets = 6 sets of predictions -> calculate all 5 metrics for each).
#       Tip: You can use `confusion_matrix(y_true, y_pred).ravel()` to easily extract 
#       True Negatives (TN), False Positives (FP), False Negatives (FN), and True Positives (TP).
#       Then compute the rates mathematically.

# Step 5: Confusion Matrices
# TODO: Create and save confusion matrices for all 3 models evaluated on both sets (6 plots total).
#       Use `ConfusionMatrixDisplay` or `matplotlib.pyplot` to visualize them.
#       Consider using a logarithmic color scale for better visibility of the minority class.
#       Save each plot to the `results/` subfolder (e.g., `results/rf_test_cm.png`).

# Step 6: Creative Analysis
# TODO: If you have time, try exploring other analysis ideas. For example:
#       - Feature importance: plot the top contributing features for the Random Forest model.
#       - Check for class imbalance. Since fraud is usually rare, should we use SMOTE, 
#         adjust class weights, or rely on Precision-Recall / F1-Scores instead of raw accuracy?
#       - Does a simple baseline model (always predicting 0) perform just as well on accuracy?

# END STUDENT IMPLEMENTATION HERE
