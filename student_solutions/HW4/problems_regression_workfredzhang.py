import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

# Ensure results directory exists relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Set random seed
np.random.seed(67)

# Generate messy data: mostly linear with gaussian noise
n_samples = 100
X = np.random.uniform(-5, 5, n_samples).reshape(-1, 1)
y = 2.5 * X.flatten() + 1.5 + np.random.normal(0, 3.0, n_samples)

# X_plot is used to draw the smooth regression lines
X_plot = np.linspace(-6, 6, 200).reshape(-1, 1)

# Dictionary to store the model predictions for plotting
# Keys should be the alpha floats (from the instruction), values should be the predicted arrays
predictions = {}

# ---------------------------------------------------------
# REGRESSION TASK
# ---------------------------------------------------------

# START STUDENT IMPLEMENTATION HERE

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_plot_scaled = scaler.transform(X_plot)

for k in [0.01, 1, 100]:
    model = Ridge(alpha=k)
    model.fit(X_scaled, y)
    pred = model.predict(X_plot_scaled)
    predictions[k] = pred


# END STUDENT IMPLEMENTATION HERE

# ---------------------------------------------------------
# PLOTTING CODE (Do not modify)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='gray', alpha=0.6, label='Data (noisy)')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
alpha_values_plot = [0.01, 1, 100]

for color, alpha in zip(colors, alpha_values_plot):
    if alpha in predictions:
        plt.plot(X_plot, predictions[alpha], color=color, 
                 label=f'Ridge $\\alpha$={alpha}', linewidth=2)

plt.title('Ridge Regression with Varying Regularization ($\\alpha$)')
plt.xlabel('X Component')
plt.ylabel('Y Target')
plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(results_dir, "regression.png"), dpi=300)
plt.close()

print(f"Regression plot generated and saved to {results_dir}")
