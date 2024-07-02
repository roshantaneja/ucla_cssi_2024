---
tags:
  - lecture
  - notes
  - summer
---
## Lecture Notes on Model Evaluation and Selection

### Key Concepts
1. **Model Evaluation**:
   - How to decide if a model is good and which model is better.

2. **Error Evaluation**:
   - Train-test split: Use training data to estimate the model and test data to evaluate the model.
   - Mean Squared Error (MSE):
     $$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
   - Mean Absolute Error (MAE):
     $$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
   - R-Squared:
     $$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$

### Overfitting
- **Definition**: A model that performs well on training data but poorly on test data.
- **Indicators**: 
  - High training accuracy but low test accuracy.
  - Model complexity is too high relative to the amount of training data.

### Model Selection
- **Process**:
  - Model Construction: Use training data to find the best parameters.
  - Model Selection: Use validation data to select the best model.
  - Model Usage: Apply the model to unseen test data.

- **Methods**:
  - Stepwise Selection: Forward selection, backward elimination.
  - Cross Validation:
    - K-Fold Cross Validation:
      $$ \text{CV}(k) = \frac{1}{k} \sum_{i=1}^{k} \text{MSE}_{i} $$
    - Leave-One-Out Cross Validation (LOOCV):
      $$ \text{LOOCV} = \frac{1}{n} \sum_{i=1}^{n} \text{MSE}_{-i} $$

### Bias vs. Variance
- **Bias**:
  - Error due to the model's assumptions.
  - High bias can cause underfitting.
- **Variance**:
  - Error due to the model's sensitivity to small fluctuations in the training set.
  - High variance can cause overfitting.
- **Trade-off**:
  - Balancing bias and variance is crucial for optimal model performance.

### Regularization
- **Concept**: Adding a penalty to the loss function to discourage complex models.
- **Types**:
  - LASSO (Least Absolute Shrinkage and Selection Operator):
    $$ L_{\text{LASSO}} = \text{MSE} + \lambda \sum_{j=1}^{p} |\beta_j| $$
  - Ridge Regression:
    $$ L_{\text{Ridge}} = \text{MSE} + \lambda \sum_{j=1}^{p} \beta_j^2 $$

- **Choosing \( \lambda \)**:
  - Cross-validation is used to select the optimal value of \( \lambda \).

### Practical Implementation
- **Using Python and Sklearn**:
  - Implementing regularized regression models using Python's `sklearn.linear_model`.

### Summary
- Model evaluation involves using metrics like MSE, MAE, and R-squared.
- Avoid overfitting through proper model selection techniques like cross-validation.
- Balance bias and variance for optimal model performance.
- Use regularization techniques like LASSO and Ridge Regression to improve model robustness.