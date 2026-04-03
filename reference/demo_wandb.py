"""
Weights & Biases (W&B) Basic Tutorial

W&B is a developer tool designed to help you track your machine learning experiments, visualize metrics, and share your findings.

If you are a total beginner, here is how you get started:
1. Create an account: Go to wandb.ai (https://wandb.ai/site) and sign up for a free account.
2. Get your API Key: Once logged in, go to your account settings (usually under your profile icon -> Settings), and scroll down to the **API keys** section. Copy your API key.
3. Install the library: Run `pip install wandb` in your environment.
4. Authenticate: You can authenticate by running `wandb login` in your terminal and pasting your key, or log in programmatically via Python (which we will show below).

Alternative to manual login, you can set an environment variable in your terminal before running your code:
`export WANDB_API_KEY="your_api_key_here"` (Linux/Mac) or `set WANDB_API_KEY="your_api_key_here"` (Windows).

Let's get started!
"""

import wandb
import numpy as np

# Authenticate with W&B
# If you set the WANDB_API_KEY environment variable, you don't need this
# Otherwise, this will prompt you to paste your API key
wandb.login()

# Set random seed for reproducibility
np.random.seed(42)

"""
The Task: Logistic Regression from Scratch

We will build a simple Logistic Regression model using **only NumPy**. All steps including the forward pass and gradient descent will be transparent and done manually.

First, let's create a toy binary classification dataset.
"""

def generate_data(num_samples=1000):
    """Generates a 2D toy dataset for binary classification."""
    # Random features
    X = np.random.randn(num_samples, 2)
    
    # Create a simple decision boundary (e.g., x1 + x2 > 0)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    
    # Add some noise (flip 5% of the labels)
    flip_indices = np.random.choice(num_samples, size=int(0.05 * num_samples), replace=False)
    y[flip_indices] = 1 - y[flip_indices]
    
    return X, y

X, y = generate_data(1000)

# Split into train and validation sets (80/20)
split_idx = int(0.8 * len(X))
X_train, y_train = X[:split_idx], y[:split_idx]
X_val, y_val = X[split_idx:], y[split_idx:]

print(f"Train set: X={X_train.shape}, y={y_train.shape}")
print(f"Validation set: X={X_val.shape}, y={y_val.shape}")

"""
Helper Functions

We need the sigmoid function for predictions, Binary Cross-Entropy (BCE) to calculate our loss, and a function to calculate accuracy.
"""

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def binary_cross_entropy(y_true, y_pred):
    # Clip predictions to avoid log(0) which results in NaN
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def compute_accuracy(y_true, y_pred_prob):
    predictions = (y_pred_prob >= 0.5).astype(int)
    return np.mean(predictions == y_true)

"""
Training the Model & Tracking with W&B

Below is the core of our tutorial. We will initialize a W&B run using `wandb.init()`, saving our hyperparameters inside the `config`.
During the training loop, we will calculate 4 metrics:
1. Train Loss
2. Validation Loss
3. Train Accuracy
4. Validation Accuracy

We then send these up to W&B using `wandb.log()`.
"""

# 1. Initialize a W&B run
run = wandb.init(
    # entity="your-team-name",                # Optionally specify which team to log to
    project="wandb-demo-logistic-regression", # The project name groups your runs together
    name="numpy-scratch-run",                 # Name for this specific run
    config={                                  # Track hyperparameters and metadata
        "learning_rate": 0.5,
        "epochs": 50,
        "architecture": "Logistic Regression (NumPy)",
        "dataset_size": len(X_train),
        "random_seed": 42
    }
)

# Access hyperparams through wandb.config
config = wandb.config

# Initialize weights (W) and bias (b)
W = np.zeros(X_train.shape[1])
b = 0.0

print("Starting training loop...")
for epoch in range(config.epochs):
    # ---------- FORWARD PASS ----------
    # Training set predictions
    z_train = np.dot(X_train, W) + b
    pred_train = sigmoid(z_train)
    
    # Validation set predictions
    z_val = np.dot(X_val, W) + b
    pred_val = sigmoid(z_val)
    
    # ---------- COMPUTE METRICS ----------
    train_loss = binary_cross_entropy(y_train, pred_train)
    train_acc = compute_accuracy(y_train, pred_train)
    
    val_loss = binary_cross_entropy(y_val, pred_val)
    val_acc = compute_accuracy(y_val, pred_val)
    
    # ---------- BACKWARD PASS (Gradient Descent) ----------
    dz = pred_train - y_train
    dW = np.dot(X_train.T, dz) / len(X_train)
    db = np.sum(dz) / len(X_train)
    
    W -= config.learning_rate * dW
    b -= config.learning_rate * db
    
    # ---------- W&B LOGGING ----------
    # 2. Log all metrics to W&B as a dictionary
    wandb.log({
        "epoch": epoch,
        "train/loss": train_loss,
        "train/accuracy": train_acc,
        "val/loss": val_loss,
        "val/accuracy": val_acc
    })
    
    # Print progress to the console periodically
    if epoch % 10 == 0 or epoch == config.epochs - 1:
        print(f"Epoch {epoch:2d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.4f}")

# 3. Finish the run properly
wandb.finish()

print("\nTraining complete! Go to your wandb dashboard to view the generated charts.")
