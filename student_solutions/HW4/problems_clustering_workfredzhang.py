import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Ensure results directory exists relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Set random seed
np.random.seed(67)

# Generate messy data: 4 distinct gaussians
n_samples_per_cluster = 100
centers = [(-3, -1), (3, -2), (0, 3), (3, 3)]
X_list = []
for center in centers:
    # Adding variance variance to make them spread but visually distinct
    X_list.append(np.random.normal(loc=center, scale=1.0, size=(n_samples_per_cluster, 2)))

X = np.vstack(X_list)

# Dictionary to store the cluster assignments
# Keys should be the integer k, values should be the array of cluster labels
assignments = {}

# ---------------------------------------------------------
# CLUSTERING TASK
# ---------------------------------------------------------

# START STUDENT IMPLEMENTATION HERE

# TODO 1: Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# TODO 2: Run KMeans for k = 3, 4, 5
for k in [3, 4, 5]:
    kmeans = KMeans(n_clusters=k, random_state=67)
    labels = kmeans.fit_predict(X_scaled)
    assignments[k] = labels

# END STUDENT IMPLEMENTATION HERE

# ---------------------------------------------------------
# PLOTTING CODE (Do not modify)
# ---------------------------------------------------------
k_values = [3, 4, 5]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('K-Means Clustering with Varying K', fontsize=16)

for i, k in enumerate(k_values):
    ax = axes[i]
    if k in assignments:
        labels = assignments[k]
        # Using a clean color map and borders for professional look
        scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', 
                             alpha=0.7, edgecolors='none', s=40)
        ax.set_title(f'K = {k}')
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
    else:
        ax.set_title(f'K = {k} (Not implemented)')
        ax.scatter(X[:, 0], X[:, 1], c='gray', alpha=0.5, s=40)
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')

plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.savefig(os.path.join(results_dir, "clustering.png"), dpi=300)
plt.close()

print(f"Clustering plot generated and saved to {results_dir}")
