---
tags:
  - homework
---

`Homework by Roshan Taneja`

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
sum = $500,000 + $700,000 + $600,000 + $550,000
mean = sum/4
```

## 1.2 Variance and Standard Deviation

**(4pt) Exercise :** Compute variance for price in Table 1.1.
```math
#Setup
avg = mean($500,000, $700,000, $600,000, $550,000)

#Calculations
variance = (($500,000 - avg)^2 + ($700,000 - avg)^2 + ($600,000 - avg)^2 + ($550,000 - avg)^2)/3
```

**(2pt) Exercise :** Compute standard deviation for price in Table 1.1.

```math
# Setup
avg = mean($500,000, $700,000, $600,000, $550,000)

#Calculations
deviations = [(5 - 5.875), (7 - 5.875), (6 - 5.875), (5.5 - 5.875)]
squared_deviations = [(-0.875)^2, (1.125)^2, (0.125)^2, (-0.375)^2]
sum_of_squared_deviations = sum(squared_deviations)


variance = sum_of_squared_deviations/4
```
## 1.3 Normalization


## 1.4 One-hot encoding


## 1.5 The relationship between two variables

