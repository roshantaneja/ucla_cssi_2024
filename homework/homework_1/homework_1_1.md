---
tags:
  - homework
  - summer
---
`Homework Entirely Complete by Roshan Taneja`
`Calculations Verified with Coco, Aditi`
# 1. Know your data

| Area (100 sq ft) | bedroom | zipcode | price ($100K USD) |
| ---------------- | ------- | ------- | ----------------- |
| 15               | 2       | 11111   | 5                 |
| 20               | 3       | 22222   | 7                 |
| 18               | 3       | 11111   | 6                 |
| 16               | 3       | 33333   | 5.5               |
^Houspricetraining
## 1.1 Mean

**(4pt) Exercise :** Compute mean for price in Table 1.1.
``` math
# Mean of Price
prices = [$5, $7, $6, $5.5]
sum = sum(prices)
mean = sum/4
```

## 1.2 Variance and Standard Deviation

**(4pt) Exercise :** Compute variance for price in Table 1.1.
```math
# Setup
prices = [$5, $7, $6, $5.5]
# Calculations
variance = sum(map(subtract(prices, mean(prices)), square))/3
```

**(2pt) Exercise :** Compute standard deviation for price in Table 1.1.

```math
# Setup
avg = mean($5, $7, $6, $5.5)
#Calculations
deviations = [($5 - avg), ($7 - avg), ($6 - avg), ($5.5 - avg)]
squared_deviations = map(deviations, square)
sum_of_squared_deviations = sum(squared_deviations)
variance = sum_of_squared_deviations/3
standard_deviation = sqrt(variance)
```
## 1.3 Normalization

**(4pt) Exercise :** Normalize area in Table 1.1 via z-score normalization.
```math
# Setup
areas = [15, 20, 18, 16]
# Calculations
mean = (15 + 20 + 18 + 16)/4
std_dev = sqrt(sum(map(subtract(areas, mean), square))/3)
z_values = subtract(areas, mean)/std_dev
```

| Original Area | Normalized Value |
| ------------- | ---------------- |
| 15            | -1.015           |
| 20            | 1.24             |
| 18            | 0.338            |
| 16            | -.564            |

## 1.4 One-hot encoding

(4pt) Exercise: Write down the one-hot encoding for every data point for variable zipcode in Table 1.1. Hint: Fill in the table below.

| Area (100 sq ft) | bedroom | is.11111 | is.22222 | is.33333 | price ($100K USD) |
| ---------------- | ------- | -------- | -------- | -------- | ----------------- |
| 15               | 2       | 1        | 0        | 0        | 5                 |
| 20               | 3       | 0        | 1        | 0        | 7                 |
| 18               | 3       | 1        | 0        | 0        | 6                 |
| 16               | 3       | 0        | 0        | 1        | 5.5               |

## 1.5 The relationship between two variables

**(2pt) Exercise :** Are area and price correlated in Table 1.1? If yes, are they positively correlated or negatively correlated?

I know they're correlated just by looking at the data. As the Area increases, the price also increases. But lets just prove it just for good measure. Im bored.

| Area (100 sq ft) | price ($100K USD) |
| ---------------- | ----------------- |
| 15               | 5                 |
| 20               | 7                 |
| 18               | 6                 |
| 16               | 5.5               |

```math
# Setup
areas = [15, 20, 18, 16]
prices = [5, 7, 6, 5.5]

# Calculate Means
mean_area = mean(areas)
mean_price = mean(prices)

# Calculate Covariance
dev_area = subtract(areas, mean_area)
dev_price = subtract(prices, mean_price)
covariance = multiply(dev_area, dev_price)/4

# Calculate Standard Deviations
std_area = std(areas)
std_price = std(prices)

# Calculate Correlation
r = covariance/(std_area * std_price)
```

Yes, Area and price are pretty __Positively Correlated__ 