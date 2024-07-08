---
tags:
  - notes
  - lecture
  - summer
  - CS
---
## Lecture Notes on Logistic Regression

### Key Concepts
1. **Classification**:
   - Categorical response variable
   - Move from numerical prediction to classification

2. **Advertising and Heart Data**:
   - Example datasets used for illustrating concepts.

3. **Binary Response and Simple Logistic Regression**:
   - Binary outcome examples (e.g., presence of heart disease: Yes/No)
   - Logistic regression for binary classification

### Binary Classification
- **Simple Logistic Regression**:
  - Logistic regression models the probability of the binary response variable as:
    $$ P(Y = 1 | X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X)}} $$
  - **Logistic Function / Sigmoid Function**:
    $$ \sigma(x) = \frac{1}{1 + e^{-x}} $$

- **Log-Odds**:
  - The logistic model can be rewritten to show log-odds:
    $$ \ln \left(\frac{P(Y=1)}{1 - P(Y=1)}\right) = \beta_0 + \beta_1X $$

### Bernoulli Distribution
* Probability of $Y = 1: p$
* probability of $Y = 0: 1-p$
* The likelihood of a single observation for $p$ given $x$ and $y$ is:
	* $$P(Y=y) = p^y(1-p)^{(1-p)}$$
* If we do this for all the points in the function we can calculate likelyhood across all points

### Estimation and Interpretation
- **Likelihood and Loss Function**:
  - The likelihood function for logistic regression:
    $$L(\beta) = \prod_{i=1}^n P(Y_{i} = y_{i})$$
  - The negative log-likelihood (loss function): Run over all points
    $$ \text{Loss} = L(p|Y) = - \sum_{i=1}^{n} \left[ y_i \log(P(Y_{i} = y_i)) + (1 - y_i) \log(1 - P(Y_{i} = y_i)) \right] = \sum_{i=1}^{n} [y_{i}\log(\frac{}{1+e^{-(\beta_0)}}) $$

### Multiple Logistic Regression
- **Generalization to Multiple Predictors**:
  - For multiple predictors:
    $$ P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X_1 + \beta_2X_2 + \ldots + \beta_kX_k)}} $$

- **Interpretation**:
  - Similar to simple logistic regression, but with multiple predictors influencing the log-odds.

### Classification Boundaries
- **Decision Boundaries**:
  - The decision boundary for logistic regression:
    $$ x_0 + \beta_1x_1 + \beta_2x_2 = 0 $$
  - Classify observations based on the predicted probabilities.

### Multiclass Logistic Regression
- **Extension to More Than Two Classes**:
  - Multinomial logistic regression:
    $$ P(Y=k|X) = \frac{e^{\beta_k'X}}{\sum_{j=1}^K e^{\beta_j'X}} $$
  - One class is chosen as the baseline, and others are compared to it.

### Applications and Examples
- **Examples of Classification in Medical Data**:
  - Predicting disease presence based on medical test results.
  - Classifying patients based on genomic markers.

### Practical Implementation
- **Using Python and Sklearn**:
  - Fitting logistic regression models using Python's `sklearn.linear_model.LogisticRegression`.

### Exercises
- **Probability and Odds**:
  - Calculate probabilities using the logistic model.
  - Determine decision boundaries for classification.

### Summary
- Classification involves categorical response variables.
- Logistic regression is used for binary and multiclass classification problems.
- The logistic function helps in modeling probabilities.
- Understanding and interpreting logistic regression models are crucial for effective classification.