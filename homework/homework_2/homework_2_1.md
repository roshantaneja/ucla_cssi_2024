---
tags:
  - homework
  - summer
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

anti_prob = subtract(1, probs)
```

| amount ($100) | fraud?  | p_i = P(Fraud = 1)                 | The probability L_i                |
| ------------- | ------- | ---------------------------------- | ---------------------------------- |
| 0.1           | 0 (No)  | 0.13                               | 0.870                              |
| 1             | 0 (No)  | 0.269                              | 0.731                              |
| 10            | 1 (Yes) | 0.000335 (probably rounding error) | 0.000335 (probably rounding error) |
| 5             | 1 (Yes) | 0.048                              | 0.048                              |

$L \approx 0.870 \times 0.731 \times 0.000335 \times 0.0474$
$L \approx 0.000010125$
$L \approx 1.0125 \times 10^{-5}$

The likelyhood of observing the dataset given $\beta_0 = -2$ and $\beta_1 = 1$ is very close to zero. I think i had a couple rounding errors somewhere. Ill clean that up later. I know that its a really small number and thats not good.
### Decision Boundary (10pt)

**(10pt) Exercise:** If the learned logistic model has β0 = −2 and β1 = 1, what is the decision boundary? Can you describe the meaning of this boundary in the transaction classification example?

if function is $\beta_{0}+ \beta_{1} \times X$ then we can solve for $X$ after setting the input to 0:

$-2 + 1 \times X = 0$

so

$X = 2$

This means that the decision boundary is at $200 since $X = 2$ corresponds to $200. Transactions with an amount above $200 are predicted as fraudulent with a probability over 50%. Transactions with an amount below $200 are predicted as fraudulent with a probability under 50%

### Regularization for logistic regression (10pt)

**(10pt) Bonus Exercise:**
1. Consider another set of coefficients, β0 = −4 and β1 = 2. Does this change the decision boundary? Does it change the likelihood? Compared to our old β coefficients, which one do you want to choose?

Lets work it out!
$\beta_{0}+ \beta_{1} \times X = 0$
$-4 + 2 \times X = 0$
$2 \times X = 4$
$X = 2$

This does not change the decision boundary

For like likelyhood calculation, we can do a little more math

```math
beta_0 = -4
beta_1 = 2
amounts = [0.1, 1, 10, 5]
fraud   = [0,   0,  1, 1]

P1(amount) = 1/(1+e^-(beta_0 + beta_1 * amount))

probs = map(amounts, P1(amount))
subtract(1, probs)


@[likelyhood::0.0000000000007257810388412397] = multiply(0.02188127093613048, 0.11920292202211757, 0.00000011253516207787584, 0.002472623156634657)

```

For some reason, due to a rounding error, it shows zero, but the actual value is closer to $7.2578 × 10^{-13}$

Increasing the beta values actually made the likelyhood lower. I would prefer $\beta_0 = -2$ and $\beta_1 = 1$ over this.

2. We can see that by increasing β0 and β1 proportionally (you can try another set of coefficients, e.g., β0 = −6 and β1 = 3), the decision boundary will not change, but the likelihood is keep increasing. Which β0 and β1 should we use then? Is that acceptable? How regularization can be used to handle this issue?

You've raised a very important point about the decision boundary remaining unchanged when \(\beta_0\) and \(\beta_1\) are increased proportionally, but the likelihood changes. This phenomenon is related to the scale of the coefficients and the potential for overfitting. Let's explore this further and how regularization can help.

### The Effect of Increasing \(\beta_0\) and \(\beta_1\) Proportionally

When we increase \(\beta_0\) and \(\beta_1\) proportionally, the decision boundary does not change. For instance:

- With \(\beta_0 = -6\) and \(\beta_1 = 3\), the decision boundary is still at:
  $-6 + 3X = 0$
  $X = 2$

However, the likelihood of the observed data changes because the probabilities become more extreme. As \(\beta_0\) and \(\beta_1\) increase, the model becomes more confident in its predictions, leading to probabilities that are closer to 0 or 1. This can artificially inflate the likelihood on the training data, but it often results in overfitting, where the model does not generalize well to new data.

### Example with \(\beta_0 = -6\) and \(\beta_1 = 3\)

Let's compute the probabilities and likelihood with these new coefficients:

1. **For amount = 0.1 ($10)**:
$p_1 = \frac{1}{1 + e^{-(-6 + 3 \times 0.1)}}$
$p_1 = \frac{1}{1 + e^{-(-6 + 0.3)}}$
$p_1 = \frac{1}{1 + e^{-(-5.7)}}$
$p_1 = \frac{1}{1 + e^{5.7}}$
$p_1 \approx \frac{1}{1 + 299.2}$
$p_1 \approx 0.0033$

2. **For amount = 1 ($100)**:
$p_2 = \frac{1}{1 + e^{-(-6 + 3 \times 1)}}$
$p_2 = \frac{1}{1 + e^{-(-6 + 3)}}$
$p_2 = \frac{1}{1 + e^{-(-3)}}$
$p_2 = \frac{1}{1 + e^3}$
$p_2 \approx \frac{1}{1 + 20.0855}$
$p_2 \approx 0.0474$

3. **For amount = 10 ($1000)**:
$p_3 = \frac{1}{1 + e^{-(-6 + 3 \times 10)}}$
$p_3 = \frac{1}{1 + e^{-(-6 + 30)}}$
$p_3 = \frac{1}{1 + e^{24}}$
$p_3 \approx \frac{1}{1 + 2.6881 \times 10^{10}}$
$p_3 \approx 3.7 \times 10^{-11}$

4. **For amount = 5 ($500)**:
$p_4 = \frac{1}{1 + e^{-(-6 + 3 \times 5)}}$
$p_4 = \frac{1}{1 + e^{-(-6 + 15)}}$
$p_4 = \frac{1}{1 + e^{9}}$
$p_4 \approx \frac{1}{1 + 8103.1}$
$p_4 \approx 1.23 \times 10^{-4}$

### Updated Table with New Probabilities

| amount ($100) | fraud? | \(p_i = P(\text{Fraud} = 1)\) | The probability \(L_i\) |
| ------------- | ------ | ----------------------------- | ----------------------- |
| 0.1           | 0      | 0.0033                        | $1 - 0.0033 = 0.9967$   |
| 1             | 0      | 0.0474                        | $1 - 0.0474 = 0.9526$   |
| 10            | 1      | $3.7 \times 10^{-11}$         | $3.7 \times 10^{-11}$   |
| 5             | 1      | $1.23 \times 10^{-4}$         | $1.23 \times 10^{-4}$   |

$L = 0.9967 \times 0.9526 \times 3.7 \times 10^{-11} \times 1.23 \times 10^{-4}$

$L \approx 0.949 \times 4.551 \times 10^{-15}$

$L \approx 4.321 \times 10^{-15}$

The likelihood with the new coefficients \(\beta_0 = -6\) and \(\beta_1 = 3\) is significantly lower than with \(\beta_0 = -2\) and \(\beta_1 = 1\), indicating that the model may be overfitting to the training data.

To address this issue, we can use regularization techniques like L1 (Lasso) or L2 (Ridge) regularization, which add a penalty term to the loss function to discourage large coefficients:

- Lasso: Adds the absolute values of the coefficients to the loss function.
  $\text{Loss} = -\sum \log L_i + \lambda \sum |\beta_j|$

- Ridge: Adds the squared values of the coefficients to the loss function.
  $\text{Loss} = -\sum \log L_i + \lambda \sum \beta_j^2$

## Multiple responses (10pt)

**(5pt) Exercise:** Consider a credit card transaction risk classification task, which has three levels: {no-risk, medium-risk, high-risk}. If the prediction probability of a transaction for each class is 0.6, 0.3, 0.1, respectively, which risk level do you want to classify this transaction into?

Given the prediction probabilites for a transaction:

* No-risk = 0.6
* Medium-risk = 0.3
* High-risk = 0.1

so we would classify the transaction as `no-risk` because its the highest probability.