---
tags:
  - summer
  - homework
  - CS
---
`Roshan Taneja`
`Worked together with Ben, Sid and Avie`
`July 5th, 2024`

# 1 (20pt) Classification Evaluation

For binary classification, a confusion matrix (table) records the number of True Positives (TP), False Negatives (FN), False Positives (TP), and True Negatives (TN). Based on a confusion matrix, different evaluation metrics can be computed. Assuming a logistic regression model gives us the following predicted probability for heart disease, work out the following exercises.

| Observed class label (Y) | Predicted probability for heart disease (P(Y= 1)) |
| ------------------------ | ------------------------------------------------- |
| 1                        | 0.9                                               |
| 1                        | 0.8                                               |
| 0                        | 0.7                                               |
| 1                        | 0.65                                              |
| 1                        | 0.6                                               |
| 0                        | 0.55                                              |
| 0                        | 0.45                                              |
| 0                        | 0.4                                               |
| 1                        | 0.35                                              |
| 0                        | 0.3                                               |
Table 1.1: A table on observed class label and predicted probability for heart disease. The positive class (with disease) is denoted as 1, and the negative class (with no disease) is denoted as 0.

---

>**(5pt) Exercise:** Given a cut-off probability 0.5, i.e., classify a data point into positive class if the predicted probability is bigger than or equal to 0.5, and classify a data point into negative class if the predicted probability is less than 0.5, fill in the confusion table below.

|                  | Predicted class = 1 | Predicted class = 0 |
| ---------------- | ------------------- | ------------------- |
| Actual class = 1 | 4                   | 1                   |
| Actual class = 0 | 2                   | 3                   |
Table 1.2: Confusion Table

---

>**(5pt) Exercise:** Calculate Accuracy, Error, Precision, Recall, andF 1 score.

```math
TP = 4
TN = 3
FP = 2
FN = 1

accuracy = (TP + TN)/(TP + TN + FP + FN)

error_rate = 1 - accuracy

precision = TP/(TP+FP)

recall = TP/(TP + FN)

f1_score = 2 * (precision * recall)/(precision + recall)
```

---

>**(5pt) Exercise:** Suppose a different logistic regression model gives us a different prediction result, and the class labels for the sorted training point (descending with predicted probability) are shown below (Table 1.3). What will the ROC curve look like? What is the area under ROC curve in this case?

| Observed class label (Y) | Predicted probability for heart disease (P(Y= 1)) |
| ------------------------ | ------------------------------------------------- |
| 1                        | 0.9                                               |
| 1                        | 0.8                                               |
| 1                        | 0.7                                               |
| 1                        | 0.65                                              |
| 1                        | 0.6                                               |
| 0                        | 0.55                                              |
| 0                        | 0.45                                              |
| 0                        | 0.4                                               |
| 0                        | 0.35                                              |
| 0                        | 0.3                                               |
Table 1.3: A table on observed class label and predicted probability for heart disease. The positive class (with disease) is denoted as 1, and the negative class (with no disease) is denoted as 0.

Given Table 1.3, we have:

| Observed class label (Y) | Predicted probability for heart disease (P(Y=1)) |
| ------------------------ | ------------------------------------------------ |
| 1                        | 0.95                                             |
| 1                        | 0.8                                              |
| 1                        | 0.7                                              |
| 1                        | 0.65                                             |
| 1                        | 0.6                                              |
| 0                        | 0.55                                             |
| 0                        | 0.45                                             |
| 0                        | 0.4                                              |
| 0                        | 0.35                                             |
| 0                        | 0.3                                              |

| Threshold | TPR | FPR |
| --------- | --- | --- |
| 0.95      | 0.2 | 0.0 |
| 0.8       | 0.4 | 0.0 |
| 0.7       | 0.6 | 0.0 |
| 0.65      | 0.8 | 0.0 |
| 0.6       | 1.0 | 0.0 |
| 0.55      | 1.0 | 0.2 |
| 0.45      | 1.0 | 0.4 |
| 0.4       | 1.0 | 0.6 |
| 0.35      | 1.0 | 0.8 |
| 0.3       | 1.0 | 1.0 |

We can use the trapezoid rule to calculate the area under the curve
$$
\text{AUC} = \frac{1}{2} \sum_{i=1}^{n-1} (FPR_{i+1} - FPR_i) \times (TPR_i + TPR_{i+1})
$$

so doing the math looks something like this
```math
(1/2) ((0.0 - 0.0) * (0.2 + 0.4) + (0.0 - 0.0) * (0.4 + 0.6) + (0.0 - 0.0) * (0.6 + 0.8) + (0.0 - 0.0) * (0.8 + 1.0) + (0.2 - 0.0) * (1.0 + 1.0) + (0.4 - 0.2) * (1.0 + 1.0) + (0.6 - 0.4) * (1.0 + 1.0) + (0.8 - 0.6) * (1.0 + 1.0) + (1.0 - 0.8) * (1.0 + 1.0))
```

So, the AUC for this ROC curve is 1. The shape of the ROC is a square. We can see that it is a perfect classification.

---

>**(5pt) Exercise:** If a binary classification task has an imbalanced label, which evaluation metrics is better, accuracy or area under ROC curve? Why? (Hint: consider a case where only 1% of the data points are positive and a random classifier.)

Accuracy is not a reliable metric for biased datasets. It can be high even with a garbage model because it can ignore the smaller class and still score highly in the majority class.

AUC is a better metric because it can focus on the ability to differentiate between classes, despite any imbalances.

---

# 2 (20pt) K Nearest Neighbor (KNN)

KNN is an algorithm that makes prediction based on a data point’s K nearest neighbors.

## 2.1 KNN for Regression

>**(10pt) Exercise:** Consider the house price dataset in Table 2.1, and answer the following questions. What are the 2 nearest neighbors for a new house with living area 1700 sq.ft. and 3 bedrooms, in terms of Euclidean distance? Based on these two neighbors, what is your prediction for its price?

| Area (100 sq ft) | bedroom | price ($100K USD) |
| ---------------- | ------- | ----------------- |
| 15               | 2       | 5                 |
| 20               | 3       | 7                 |
| 18               | 3       | 6                 |
| 16               | 3       | 5.5               |
Table 2.1: House Price Training Dataset

```math
dist(x2, y2) = sqrt((x2-17)^2 + (y2-3)^2)

h1 = dist(15, 2)
h2 = dist(20, 3)
h3 = dist(18, 3)
h4 = dist(16, 3)

# Closest houses are h3 and h4

price_avg = (6+5.5)/2
```

predicted price around $575,000

---

## 2.2 KNN for Classification

>**(5pt) Exercise:** Consider the credit card transaction dataset in Table 2.2, for a new transaction with $250 amount, what are the 3 nearest neighbors to it? Based on these 3 nearest neighbors, what is its probability to be a fraud? Based on this probability, do you classify it into fraud or not?

```math
dist(x) = abs(2.5-x)

dist(0.1)
dist(1)
dist(2)
dist(3)
dist(5)
dist(10)

# 3 closest neighbors are 1, 2 and 3

prob = (0+0+1)/3
```

The probability that the transaction is fraud is around 33%. Based on this probability, I would not classify it as fraud.

---
## 2.3 Selecting K

>**(5pt) Exercise:** When K becomes bigger, does the model become more complex or simpler? For the classification case, when K becomes bigger, does the decision boundary become smoother or more bumpy? How do you decide K in practice?

| amount ($100) | fraud?  |
| ------------- | ------- |
| 0.1           | 0 (No)  |
| 1             | 0 (No)  |
| 2             | 0 (No)  |
| 3             | 1 (Yes) |
| 5             | 1 (Yes) |
| 10            | 1 (Yes) |
Table 2.2: Credit Card Transaction Dataset

as the K value gets greater, the KNN model becomes simpler. As the K value gets smaller, the KNN model becomes more "bumpy".

We can identify the right K value using cross-validation to assess the accuracy of each K value.

---
# 3 (20pt + 5 bonus pt) Support Vector Machine (SVM)

Linear SVM aims at finding the best linear form decision boundary to separate two classes. In the case where we have two predictors,$X_{1}$ and$X_2$ , the decision boundary can be written as a line:

$$\omega_{1}X_{1} + \omega_{2}X_{2} + b = 0$$

The closest data points to the decision boundary are called support vectors. The goal is to maximize the distance between support vectors to the decision boundary, or equivalently the distance between two lines spanned by support vectors in each of the two classes, which is called `margin`.

## 3.1 Linear SVM

> **(5pt) Exercise:** In the linearly separable case, where positive class and negative class points can be completely separated by a line, how many lines are there with a training error 0?

There are infinitely many possible lines that can separate the 2 classes with a training error of 0 because it is linearly separable.

---

>**(5pt) Exercise:** Suppose there are two lines, one is with margin 5 and the other is with margin 4, for the same training dataset, which one do you want to choose? Why?

You wanna choose the line with boundary 5 because the larger margin makes the model more accurate with noise and larger variation in the testing and validation data. The goal of the SVM is to maximize the margin.

---

>**(5pt) Exercise:** Suppose we have a decision boundary $X_{1} +X_{2} −1 = 0$ for a binary classification task, and a data point with$x_{1} = 1$ and $x_{2} = 1$, which class should we classify it into, positive or negative? Why?

```math
# Plug in the values
x1 = 1
x2 = 1


x1 + x2 - 1

# That was easy.
```

The data point with  $x_1 = 1$  and  $x_2 = 1$  should be classified into the positive class because  $X_1 + X_2 - 1 = 1$  is greater than 0, indicating that it lies on the positive side of the decision boundary.

---

>**(5pt) Bonus Exercise:** Suppose we have identified three support vectors through some optimizer, which are (1,0), (0,1) with positive label, and (0,0) with negative label. Can you write down the decision boundary based on these three support vectors? (Hint: (1) What is the line spanned by (1,0) and (0,1)? (dotted lines in our lecture slides) (2) what is the line for the negative support vector? Remember the two lines have to be parallel to each other. (3) What is the decision boundary, which has to be in the middle of those two lines?)

Positive support vectors are $(1,0)$ and $(0, 1)$. So the line is $x_{1} + x_{2} = 1$. \

This is because at  $(1,0)$ ,  $x_1 = 1$  and  $x_2 = 0$ , and at  $(0,1)$ ,  $x_1 = 0$  and  $x_2 = 1$ .

The negative support vector is  $(0,0)$ .

To find a line parallel to the line  $x_1 + x_2 = 1$  that passes through  $(0,0)$ , we can write:

$x_1 + x_2 = 0$

The midway line between $x_1 + x_2 = 1$  and  $x_1 + x_2 = 0$  is:

$x_1 + x_2 = 0.5$

Decision Boundary

Therefore, the decision boundary based on the given support vectors  $(1,0)$ ,  $(0,1)$  with positive labels and  $(0,0)$  with a negative label is:

$x_1 + x_2 = 0.5$

---
## 3.2 Kernel SVM

When the dataset is not linearly separable, meaning there is no way to use a line to partition data points from two classes into two sides, we can use kernel SVM. The idea behind Kernel SVM is to transform a data point to an even higher dimensional space. For example, from $(x_{1}, x_{2})$ to $(x_{1}, x_{2}, \sqrt{x_{1}^2+x_{2}^2})$. This transformation might be very complicated and hard to design. In practice, what we really need to know is a kernel function that tells us the similarity between any two data points. For example, we can define the similarity between two data points $x_{i} = (x_{i1}, x_{i2})$ and $x_{i} = (x_{j1}, x_{j2})$ using polynomial kernel with degree 2:

$$K(xi,xj) = (x_{i1}x_{j1} +x_{i2}x_{j2} + 1)^2$$

>**(5pt) Exercise:** Given three data points, $(1,1)$, $(-1,0)$, and $(-1,1)$, which point is more similar to $(1,1)$ according to the polynomial kernel with degree 2 defined above?

```math

K(xi, yi, xj, yj) = (xi*xj + yi*yj + 1)^2

K(1, 1, 1, 1)

K(1, 1, -1, 0)

K(1, 1, -1, 1)
```

The point $(-1,1)$ is more similar to $(1,1)$ compared to the point $(-1,0)$ according to the polynomial kernel with degree 2, as the similarity score $K((1,1), (-1,1)) = 1$ is greater than $K((1,1), (-1,0)) = 0$.

---
## 4 (20pt) Decision Tree

Decision Tree is an algorithm that divides the data into different regions, which correspond to leaf nodes in a tree structure, and the decisions will be made based on the prediction on the specific region a data belongs to.

To construct a tree, we need to choose the “best” predictor to split the data. If the predictor is categorical, the splitting is based on the categorical values; if the predictor is numerical, we also need to decide the cut-off value.

>**(10pt) Exercise:** Consider a dataset with two predictors Ages and CreditRating, with the goal to classify whether a person is going to purchase xbox. The class labels are shown for data points in each partition after splitting for both Ages and CreditRating in Fig. 4.1. (1) Calculate weighted average classification error for both Ages and CreditRating, with the help of Table 4.1 and Table 4.2. (Some of the numbers are provided.) (2) Which predictor do you want to choose for the splitting?

Let's fill out the tables with the appropriate values and then recalculate the weighted average classification errors to ensure accuracy.

### Table 4.1: Ages
| Class = Yes | Class = No | Classification Error for each Region | Weight of each Region |
|-------------|------------|--------------------------------------|-----------------------|
| 2           | 3          | 2/5                                  | 5/14                  |
| 5           | 0          | 0/5                                  | 5/14                  |
| 3           | 3          | 3/6                                  | 6/14                  |

### Table 4.2: Credit Rating
| Class = Yes | Class = No | Classification Error for each Region | Weight of each Region |
|-------------|------------|--------------------------------------|-----------------------|
| 4           | 3          | 3/7                                  | 7/15                  |
| 5           | 3          | 3/8                                  | 8/15                  |


```math
# For Ages: Weighted Average Classification Error
Error = ((5/16) * (3/5)) + ((5/16)*0) + ((6/16) * (3/6))
```

```math
# For Credit Rating: Weighted Average Classification Error
Error = ((7/15)*(3/7)) + ((8/15)*(3/8))
```

The weighted average classification error for Ages is approximately $0.357$, while for Credit Rating it is $0.4$. Therefore, Ages should be chosen as the predictor for splitting.

---

>**(10pt) Exercise:** Given a regression tree as shown in Fig. 4.2, predict the salary for a baseball player with 5 years service and 150 hits. (left branches mean yes and right branches mean no.) Explain your reasons.

The player has 5 years of service so it goes to the right. Next, since 150 hits is more than 117.5, we move to the right again. We reach a leaf node of $6.74$ which im assuming is $674,000.

---

# 5 (20pt) Neural Networks

A neural network defines a function that maps an input vector to an output vector. The function is determined by the architecture of the neural network, and the activation functions of each neuron. The parameters of the network are weights on the connections between neurons as well as the bias terms associated with each neuron. Training a neural network involves (1) a forward step, where predictions are calculated in a forward fashion for a mini-batch of inputs; and (2) a backpropagation step, where predictions are compared with the observed labels and the loss is propagated backward to update param-
eters involved in each layer. The two steps are repeated iteratively until convergence or early stopping (based on validation dataset).

>**(10pt) Exercise:** For a fully connected multi-layer feed-forward neural network with 1 input layer (3 units), 2 hidden layers (4 units and 4 unites), and one output layer (3 units), how many parameters are there in total?

input to second layer: Weights 3 * 4 = 12

second to third = 4 * 4 = 16

third to output = 4 * 3 = 12

weights = 4 + 4 + 3 = 11

**total** = 51 parameters

---

>**(10pt) Exercise:** Given a neural network architecture shown in Fig. 5.1, weights and bias shown in Table 5.1, and activation function for all neurons as ReLU function, compute the output for the input data point (0,1).

Datapoints (0, 1)

output from 1: 0

output from 2: 1

output from 3: (-0.3 * 0) + (0.4 * 1) = 0.4 + 0.2 = 0.6

output from 4: (0.2 * 0)(-0.1 * 1) = -0.1 - 0.4 = -0.5 = 0

input to 5: (-0.12) + (0) = 0 + 1

**output from 5:** 0