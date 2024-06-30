---
tags:
  - homework
---

# Instruction and preparation

| Area (100 sq ft) | bedroom | zipcode | price ($100K USD) |
| ---------------- | ------- | ------- | ----------------- |
| 15               | 2       | 11111   | 5                 |
| 20               | 3       | 22222   | 7                 |
| 18               | 3       | 11111   | 6                 |
| 16               | 3       | 33333   | 5.5               |


# Linear regression (45pt)

## Simple linear Regression (40pt)

### The form of simple linear regression (5pt)


**(5pt) Exercise:** Given β0 = 1 and β1 = 3, what would be our price prediction for a house with 1500 sq.ft. (i.e., area = 15)?
```math
beta_0 = 1
beta_1 = 3

area = 1500/100

price = beta_0 + beta_1 * area
```


### Estimating parameters using training dataset (25pt)

**(15pt) Exercise:** Suppose we have two possible lines to fit the data in Table 0.1. For the first line, β0 = 1 and β1 = 3; and for the second line, β0 = 2 and β1 = 2. Please fill in the following table (Table 1.1). What is the MSE for each line? Which line will you choose and why?

```math
beta_0 = 1
beta_1 = 3

areas = [15, 20, 18, 16]
prices = [5, 7, 6, 5.5]

# Pred Line 1
pred = add(multiply(areas, beta_1), beta_0)

residuals = subtract(prices, pred)

mse = sum(map(residuals, square))/4
```

```math
beta_0 = 2
beta_1 = 2

areas = [15, 20, 18, 16]
prices = [5, 7, 6, 5.5]

# Pred Line 2
pred = add(multiply(areas, beta_1), beta_0)

residuals = subtract(prices, pred)

mse = sum(map(residuals, square))/4
```

| True Price | Pred Line 1 | Res Line 1 | Pred Line 2 | Res Line 2 |     |
| ---------- | ----------- | ---------- | ----------- | ---------- | --- |
| 5          | 46          | -41        | 32          | -27        |     |
| 7          | 61          | -54        | 42          | -35        |     |
| 6          | 55          | -49        | 38          | -32        |     |
| 5.5        | 49          | -43.5      | 34          | -28.5      |     |

Based on the MSE, Line 2 has a lower MSE (947.56) compared to Line 1 (2222.56). Therefore, we would choose Line 2 because it has a smaller MSE, indicating that it fits the data better.

**(10pt) Exercise:** Find the best β0 and β1. You can use any approach you like, for example, calculating by hand using closed form formula provided in lecture slides or coding (e.g., code from Homework 2 Part 2). Calculate MSE for this best-fit line. Is it indeed smaller than Line 1 and 2?

```math
areas = [15, 20, 18, 16]
prices = [5, 7, 6, 5.5]

# Calc Beta Values
x_bar = sum(areas)/4
y_bar = sum(prices)/4

beta_1 = subtract(areas, x_bar)*subtract(prices, y_bar)/sum(map(subtract(areas, x_bar), square))

beta_0 = y_bar - beta_1 * x_bar

# Our best line fit is:
price_pred(x) = beta_0 + beta_1 * x

preds = price_pred(areas)

residuals = prices - preds

mse = sum(map(residuals, square))/4
```

the MSE is significantly smaller than lines 1 and 2 by nearly 4 orders of magnitude.

### Model evaluation (10pt)

**(10pt) Exercise:** Based on the above test dataset, evaluate your model derived from previous exercise using MSE. Note, this is called test MSE, in contrast to train MSE in the previous exercise. Please use the following table to help your calculation.

| Area (100 sq ft) | price ($100k) |
| ---------------- | ------------- |
| 25               | 8             |
| 12               | 4             |

```math
# Generate Model
areas = [15, 20, 18, 16]
prices = [5, 7, 6, 5.5]
x_bar = sum(areas)/4
y_bar = sum(prices)/4
beta_1 = subtract(areas, x_bar)*subtract(prices, y_bar)/sum(map(subtract(areas, x_bar), square))
beta_0 = y_bar - beta_1 * x_bar
price_pred(x) = beta_0 + beta_1 * x

# Assess Model

test_areas = [25, 12]
test_prices = [8, 4]

preds = price_pred(test_areas)

residuals = test_prices - preds

test_mse = sum(map(residuals, square))/2
```

| Area (100 sq ft) | Pred Price ($100k) | price ($100k) |
| ---------------- | ------------------ | ------------- |
| 25               | 8.831              | 8             |
| 12               | 3.873              | 4             |

## Multiple linear regression (5pt)

**(5pt) Exercise:** Given β0 = 1, β1 = 3, and β2 = 2, what would be our price prediction for a house with 1500 sq.ft. and 2 bedrooms (i.e., area = 15 and bedroom = 2)?

```math
beta_0 = 1
beta_1 = 3
beta_2 = 2

price(area, bedrooms) = beta_0 + beta_1 * area + beta_2 * bedrooms

@[price(15, 2)::50]

```

According to the regression, a good estimate for the house would be close to **$5,000,000**. Thats a lot!
# Logistic regression (45pt)

| amount ($100) | fraud?  |
| ------------- | ------- |
| 0.1           | 0 (No)  |
| 1             | 0 (No)  |
| 10            | 1 (Yes) |
| 5             | 1 (Yes) |

## Binary responses (30)

### The form of simple logistic regression (5pt)

**(5pt) Exercise:** Given β0 = −2 and β1 = 1, what is the probability that a transaction with amount $100 (i.e., amount = 1) is a fraud?

```math
beta_0 = -2
beta_1 = 1

P1(amount) = 1/(1+e^-(beta_0 + beta_1 * amount))

P1(1)
```
### Estimating parameters using training dataset (15pt)

**(15pt) Exercise:** Compute the likelihood of observing the dataset given β0 = −2 and β1 = 1, with the help of the following table.

| amount ($100) | fraud?  | p_i = P(Fraud = 1) | The probability L_i |
| ------------- | ------- | ------------------ | ------------------- |
| 0.1           | 0 (No)  |                    |                     |
| 1             | 0 (No)  |                    |                     |
| 10            | 1 (Yes) |                    |                     |
| 5             | 1 (Yes) |                    |                     |

```math
beta_0 = -2
beta_1 = 1
amounts = [0.1, 1, 10, 5]
fraud   = [0,   0,  1, 1]

P1(amount) = 1/(1+e^-(beta_0 + beta_1 * amount))

# Probability Calculation
probs = map(amounts, P1(amount))

P1(10)
```

| amount ($100) | fraud?  | p_i = P(Fraud = 1) | The probability L_i |
| ------------- | ------- | ------------------ | ------------------- |
| 0.1           | 0 (No)  | 0.13               | 0.870               |
| 1             | 0 (No)  | 0.269              | 0.731               |
| 10            | 1 (Yes) | 0                  | 0                   |
| 5             | 1 (Yes) | 0.048              | 0.048               |


L = 0

the likelyhood of observing the dataset given beta_0 = -2 and beta_1 = 1 is basically zero. I think i had a couple rounding errors somewhere. Ill clean that up later. I know that its a really small number and thats not good.
### Decision Boundary (10pt)

**(10pt) Exercise:** If the learned logistic model has β0 = −2 and β1 = 1, what is the decision boundary? Can you describe the meaning of this boundary in the transaction classification example?

### Regularization for logistic regression (10pt)

## Multiple responses (10pt)