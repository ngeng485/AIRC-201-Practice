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
df = df.drop(columns=['nameOrig', 'nameDest'])
df['type'] = LabelEncoder().fit_transform(df['type'])
X = df.drop(columns=['isFraud'])
y = df['isFraud']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, shuffle=True
)

# Step 3: Train Three Models
models = {
    'ridge': RidgeClassifier(alpha=1.0, solver='auto'),
    'rf': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
    'ada': AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42)
}
for name, model in models.items():
    model.fit(X_train, y_train)

# Step 4: Evaluate Models
def evaluate(y_true, y_pred, model_name, split_name):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    accuracy = accuracy_score(y_true, y_pred)
    fpr = fp / (fp + tn)
    fnr = fn / (fn + tp)
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    print(f"\n{model_name} ({split_name})")
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  TPR: {tpr:.4f}  TNR: {tnr:.4f}")
    print(f"  FPR: {fpr:.4f}  FNR: {fnr:.4f}")

for name, model in models.items():
    for split_name, X_split, y_split in [('Train', X_train, y_train), ('Test', X_test, y_test)]:
        y_pred = model.predict(X_split)
        evaluate(y_split, y_pred, name, split_name)

# Step 5: Confusion Matrices
for name, model in models.items():
    for split_name, X_split, y_split in [('train', X_train, y_train), ('test', X_test, y_test)]:
        y_pred = model.predict(X_split)
        cm = confusion_matrix(y_split, y_pred)
        fig, ax = plt.subplots(figsize=(6, 5))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot(ax=ax, colorbar=False)
        ax.set_title(f'{name} - {split_name}')
        plt.tight_layout()
        plt.savefig(os.path.join(results_dir, f"{name}_{split_name}_cm.png"), dpi=300)
        plt.close()

# Step 6: Creative Analysis
importances = models['rf'].feature_importances_
feature_names = df.drop(columns=['isFraud']).columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 5))
plt.bar(range(len(importances)), importances[indices])
plt.xticks(range(len(importances)), feature_names[indices], rotation=45, ha='right')
plt.title('Random Forest Feature Importances')
plt.tight_layout()
plt.savefig(os.path.join(results_dir, "rf_feature_importance.png"), dpi=300)
plt.close()

# Baseline
baseline_acc = accuracy_score(y_test, np.zeros(len(y_test)))
print(f"\nBaseline accuracy (always predict 0): {baseline_acc:.4f}")

# END STUDENT IMPLEMENTATION HERE
