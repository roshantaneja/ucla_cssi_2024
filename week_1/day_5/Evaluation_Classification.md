---
tags:
  - lecture
  - notes
  - summer
  - CS
---
## Lecture Notes on Classification Evaluation and Model Selection

### Key Concepts
1. Regularization in Logistic Regression
2. Model Evaluation in Classification
3. Practical Issues

### Regularization in Logistic Regression

#### Review of Linear Regression Regularization
- Objective: Minimize the sum of squared errors (MSE).
- Regularization: Adds a penalty factor, e.g., Ridge Regression:
  $$
  \text{Ridge Regression:} \quad \min \sum (y_i - \hat{y}_i)^2 + \lambda \sum \beta_j^2
  $$

#### Regularization in Logistic Regression
- Adds a penalty factor to the logistic regression loss function:
  $$
  \text{Regularized Logistic Regression:} \quad \min -\log L(\beta | X, y) + \lambda \sum \beta_j^2
  $$
  - Note: Intercept typically not penalized.

#### Log-likelihood
- Definition:
  $$
  \log L(\beta | X, y) = \sum [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]
  $$
  where $p_i = \frac{1}{1 + e^{-\beta^T x_i}}$

#### Example: Regularization in Logistic Regression
- Visual demonstration with L1 and L2 penalties.
- Selection of regularization weight through cross-validation.

#### Cross-validation
- Procedure for selecting $\lambda$:
  1. For each $\lambda$:
     - Divide data into k folds.
     - Train on k-1 folds, validate on the remaining fold.
     - Average performance across k folds.
  2. Select $\lambda$ with the highest accuracy.

### Model Evaluation in Classification

#### Classification Metric: Test Accuracy
- Accuracy:
  $$
  \text{Accuracy} = \frac{\text{Number of correctly classified samples}}{\text{Total number of samples}}
  $$

#### Training: Model Construction
- Example rule-based classifier:
  $$
  \text{IF rank} = \text{'professor'} \text{OR years} > 6 \text{ THEN tenured} = \text{'yes'}
  $$

#### Evaluation Metrics
- Holdout Method:
  - Partition data into training and test sets.
- Cross-validation (k-fold):
  - Partition data into k subsets, use each subset as test set while others are training sets.

### Beyond Accuracy: Error Analysis in Classification

#### Types of Errors
1. False Positives (FP)
2. False Negatives (FN)

#### Confusion Matrix
- Structure:
  $$
  \begin{array}{|c|c|c|}
  \hline
  & \text{Predicted Positive} & \text{Predicted Negative} \\
  \hline
  \text{Actual Positive} & TP & FN \\
  \hline
  \text{Actual Negative} & FP & TN \\
  \hline
  \end{array}
  $$
- Accuracy calculation:
  $$
  \text{Accuracy} = \frac{TP + TN}{\text{Total}}
  $$

#### Precision, Recall, and F-measures
- Precision:
  $$
  \text{Precision} = \frac{TP}{TP + FP}
  $$
- Recall:
  $$
  \text{Recall} = \frac{TP}{TP + FN}
  $$
- F-measure:
  $$
  F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  $$

### ROC Curves
- Trade-off between True Positive Rate (TPR) and False Positive Rate (FPR).
- Area Under Curve (AUC) measures model accuracy.

### Multiclass Classification
- Methods:
  1. One-vs-All (OVA): Train m classifiers for m classes.
  2. All-vs-All (AVA): Train classifiers for each pair of classes.

### Classification of Class-Imbalanced Data Sets
- Techniques for handling imbalance:
  - Oversampling minority class.
  - Undersampling majority class.
  - Synthesizing new data points (e.g., SMOTE).

### Better than Global Mean?


### Summary
- Covered regularization in logistic regression, model evaluation and selection, evaluation metrics, multiclass classification, and handling imbalanced classes.