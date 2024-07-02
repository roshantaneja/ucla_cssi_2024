---
tags:
  - lecture
  - notes
  - summer
---
## Lecture Notes on K-Nearest Neighbors (KNN)

### Content Overview
1. KNN for Regression
2. KNN for Classification
3. Model Selection for KNN

### Introduction to KNN
- **Fundamental Assumption**: Data points (as vectors) that are close by should be considered similar and have the same target prediction.

### KNN for Regression
- **Example Dataset**: Advertising data (TV, radio, newspaper, sales).
- **Simple Prediction Model**: Use the mean of the k-nearest neighbors for prediction.
- **Model Extension**: From 1 neighbor to k neighbors.

### KNN for Classification
- **Concept**: Predict the class of a sample based on the majority class among its k-nearest neighbors.
- **Formal Definition**:
  $$
  P(Y = j | X = x_0) = \frac{1}{k} \sum_{i \in N_k(x_0)} I(y_i = j)
  $$
  where \( N_k(x_0) \) is the set of k observations nearest to \( x_0 \).

### Error Evaluation for KNN
- **Train-Test Split**: Hide some data from the model to evaluate its performance.
- **Evaluation Metrics**: Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).
  $$
  MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
  $$
  $$
  RMSE = \sqrt{MSE}
  $$

### Model Selection for KNN
- **Choice of k**: The value of k significantly affects the model's predictions.
- **Bias-Variance Tradeoff**: Small k leads to high variance (sensitive to noise), large k leads to high bias (oversmoothing).
- **Cross-validation**: A principled way to select k by evaluating performance across different k values.

### Practical Issues in KNN
- **Distance Metrics**: Euclidean distance is commonly used.
  $$
  d(x_i, x_j) = \sqrt{\sum_{m=1}^p (x_{im} - x_{jm})^2}
  $$
- **Standardization**: Important to standardize predictors to handle differences in variability and mixtures of quantitative and categorical predictors.

### KNN vs Logistic Regression
- **KNN**: No training phase, but slow inference.
- **Logistic Regression**: Slower training phase, but fast inference.

### Summary
- K-nearest neighbor algorithm for prediction and classification.
- Importance of choosing an appropriate k.
- Handling multiple predictors and standardization.