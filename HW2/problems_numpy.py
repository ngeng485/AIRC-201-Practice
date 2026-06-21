import numpy as np

def relu_activation(arr: np.ndarray) -> np.ndarray:
    """
    Applies the Rectified Linear Unit (ReLU) activation element-wise.
    Returns a new array where all negative values are replaced with 0.
    """
    return np.maximum(0, arr)

def calculate_euclidean_distance(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Given two 1D arrays (vectors) of the same length, return the Euclidean distance between them.
    """
    return float(np.sqrt(np.sum((v2 - v1) ** 2)))

def matrix_multiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Returns the matrix multiplication of 2D arrays A and B.
    """
    return A @ B

def normalize_data(X: np.ndarray) -> np.ndarray:
    """
    Performs Z-score normalization on a 2D array X (samples x features).
    Returns a new array where each feature (column) has mean 0 and standard deviation 1.
    If a column has 0 standard deviation, its normalized values should be 0.
    """
    mean = X.mean(axis = 0)
    std = X.std(axis = 0)
    result = np.where(std == 0, 0, (X - mean) / std)
    return result

def one_hot_encode(labels: np.ndarray, num_classes: int) -> np.ndarray:
    """
    Converts a 1D array of integer class labels (0 to num_classes-1) to a 2D one-hot encoding matrix.
    Shape of output should be (len(labels), num_classes).
    """
    result = np.zeros((len(labels), num_classes), dtype=int)
    result[np.arange(len(labels)), labels] = 1
    return result

def softmax_activation(logits: np.ndarray) -> np.ndarray:
    """
    Applies the softmax function to a 2D array of logits (samples x classes).
    Subtract the maximum logit of each row for numerical stability.
    Returns a 2D array of probabilities where each row sums to 1.
    """
    shifted = logits - logits.max(axis = 1, keepdims = True)
    exp_vals = np.exp(shifted)
    return exp_vals / exp_vals.sum(axis = 1 , keepdims = True)

def find_k_nearest_neighbors(data: np.ndarray, query: np.ndarray, k: int) -> np.ndarray:
    """
    Given a 2D array of data points (samples x features) and a 1D query point (features),
    return the indices of the 'k' closest points in 'data' using Euclidean distance.
    """
    distances = np.sqrt(np.sum((data - query) ** 2, axis = 1))
    return np.argsort(distances)[:k]

def compute_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, num_classes: int) -> np.ndarray:
    """
    Computes a confusion matrix C of shape (num_classes, num_classes) where 
    C[i, j] is the count of observations known to be in group i and predicted to be in group j.
    """
    matrix = np.zeros((num_classes, num_classes), dtype = int)
    np.add.at(matrix, (y_true, y_pred), 1)
    return matrix

def calculate_class_centroids(X: np.ndarray, labels: np.ndarray, num_classes: int) -> np.ndarray:
    """
    Given a 2D array of data points X (samples x features) and a 1D array of labels (0 to num_classes-1),
    compute the centroid (mean vector) for each class.
    Returns a 2D array of shape (num_classes, features).
    If a class has no examples, its centroid should be an array of zeros.
    """
    centroids = np.zeros((num_classes, X.shape[1]))
    for c in range(num_classes):
        mask = labels == c
        if mask.any():
            centroids[c] = X[mask].mean(axis = 0)
        return centroids