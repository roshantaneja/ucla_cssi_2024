---
tags:
  - lecture
  - notes
---
## Lecture Notes on Linear Regression for Prediction

### Key Concepts
1. **Overview of Data Science**:
   - Data types, function types, life cycle
   - Data exploration: summary statistics, visualization, preprocessing

2. **Algorithms for Prediction**:
   - Prediction/regression
   - Classification
   - Clustering

### Prediction Problem
- **Objective**: Predict one variable using another or a set of other variables.
- **Examples**:
  - Predicting YouTube video views based on various features.
  - Predicting Netflix user movie ratings based on previous ratings and demographics.

### Linear Regression Models
1. **Simple Linear Regression**:
   - Predicting a variable \( Y \) using another variable \( X \).
   - Model: \( Y = \beta_0 + \beta_1X \)
   - Goal: Minimize the Mean Squared Error (MSE).
     $$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$

2. **Multi-variate Linear Regression**:
   - Predicting \( Y \) using multiple predictors.
   - Model: \( Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \ldots + \beta_pX_p \)
   - MSE in vector notation:
     $$ \text{MSE} = \frac{1}{n} (Y - X\beta)^T(Y - X\beta) $$
   - Solution using vector calculus:
     $$ \beta = (X^TX)^{-1}X^TY $$

3. **Polynomial Regression**:
   - Extending linear regression to capture non-linear relationships.
   - Model: \( Y = \beta_0 + \beta_1X + \beta_2X^2 + \ldots + \beta_dX^d \)
   - Minimize MSE similarly to linear regression.

### Model Estimation and Interpretation
1. **Estimating Regression Coefficients**:
   - Using Ordinary Least Squares (OLS) method.
   - Example of calculating residuals and loss:
     $$ \text{Residual} = y_i - \hat{y}_i $$
     $$ \text{Squared Error} = (\text{Residual})^2 $$
   - Using gradient descent for optimization:
     $$ \beta := \beta - \eta \nabla L(\beta) $$
     where \( \eta \) is the learning rate.

2. **Goodness of Fit**:
   - R-Squared (\( R^2 \)):
     $$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$

### Practical Considerations
1. **Training, Validation, and Test Sets**:
   - Training: Learn the model.
   - Validation: Model selection (e.g., hyperparameter tuning).
   - Test: Evaluate model performance.

2. **Qualitative Predictors**:
   - Encoding categorical variables using dummy variables.
   - One-hot encoding for variables with more than two levels.

### Advanced Topics
1. **Bootstrap for Estimating Sampling Error**:
   - Sampling with replacement to create new datasets.
   - Estimating variability and confidence intervals for model parameters.

2. **Overfitting**:
   - Model too closely fits the training data but fails on new data.
   - Indicators: High training accuracy but low test accuracy.

3. **Multicollinearity**:
   - High correlation among predictors can cause instability in estimates.
   - Solution: Regularization techniques like Ridge and LASSO.

### Summary
- **Linear Regression**:
  - Predicts response as a linear function of predictors.
  - Techniques: Simple, multi-variate, polynomial regression.
  - Evaluation: MSE, R-Squared, residual analysis.

- **Regularization**:
  - Techniques to avoid overfitting by penalizing large coefficients.
  - Ridge (L2) and LASSO (L1) regression.