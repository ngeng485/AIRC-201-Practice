# HW5 - Full Machine Learning Pipeline: Fraud Detection

This assignment focuses on a complete Machine Learning workflow using **Scikit-Learn** and **Pandas**. You will build a machine learning pipeline from scratch to detect fraudulent transactions within financial data.

## Instructions

For this homework, you will test your end-to-end data science skills by loading a real-world dataset, preprocessing the data, training multiple models, and evaluating their success using various performance metrics.
Complete the tasks specified in the following file:
1. `HW5/problems.py`

Write your machine learning code between the `# START STUDENT IMPLEMENTATION HERE` and `# END STUDENT IMPLEMENTATION HERE` comments. Note that unlike previous assignments, this homework is highly open-ended. You will need to write the majority of the data cleaning, splitting, training, and testing code yourself.

### Detecting Credit Card Fraud (`problems.py`)
In this file, you must construct a pipeline to predict whether an individual transaction is fraudulent (`isFraud`).
- **Data Preprocessing**: Analyze `data/fraud_transactions.csv`. Drop uninformative qualitative columns, encode categorical transaction types, and standardize independent features. 
- **Data Splitting**: Perform a randomized and reproducible 80/20 Train/Test split.
- **Model Training**: You have the freedom to choose your models! If undecided, we recommend exploring `RidgeClassifier`, `RandomForestClassifier`, and `AdaBoostClassifier`.
- **Model Evaluation**: You must compute the Accuracy, True Positive Rate (TPR), True Negative Rate (TNR), False Positive Rate (FPR), and False Negative Rate (FNR) for all 3 of your models on both the training and test sets. 
- **Visualization**: Generate confusion matrices for all combinations of models and datasets, and save them as images into the `HW5/results/` directory.

### Going the Extra Mile
Fraud detection often operates on highly imbalanced datasets. Think closely about the metrics you produce. Are they truly reflective of model success? Try implementing class weights, feature importance analyses, or investigating precision-recall to further strengthen your analytical toolkit!