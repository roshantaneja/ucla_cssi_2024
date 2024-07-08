---
tags:
  - notes
  - lecture
  - summer
---
## Lecture Notes on Support Vector Machines (SVM)

### Key Concepts
1. **Support Vector Machines**:
   - A supervised learning model used for classification and regression tasks.
   - Effective in high-dimensional spaces and when the number of dimensions exceeds the number of samples.

2. **Decision Boundaries**:
   - A hyperplane that separates different classes in the feature space.
   - When data is linearly separable, SVM finds the optimal hyperplane that maximizes the margin between the classes.

### Linear SVM
- **Linear Separability**:
  - Data is considered linearly separable if it can be perfectly separated by a linear boundary.
  - Multiple decision boundaries can fit the data; SVM chooses the best one by maximizing the margin.

- **Hyperplane**:
  - Defined by the equation:
   $$ w^T x + b = 0$$

- The signed distances from a point$x \in \mathbb{R}^n$ to the decision boundary is

$$ D(x) = \frac{w^{T} x + b}{||w||}$$

- $w$ is the weight vector (normal to the hyperplane) and$b$ is the bias term.

![](80_Learning_Education/82_Summer_Courses/82.30_ucla_cssi_2024/week_2/day_1/dist_to_decision_bound.png)

- **Margin**:
  - The distance between the hyperplane and the nearest data points from each class.
  - The points closest to the hyperplane are called **support vectors**.
  - SVM aims to maximize this margin.

### Mathematical Formulation
1. **Objective**:
   - Maximize the margin, which is equivalent to minimizing$\|\mathbf{w}\|$.
   - The optimization problem:
    $$ \min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2$$
     Subject to:
    $$ y_i (\mathbf{w}^T \mathbf{x}_i + b) \geq 1$$

2. **Constraints**:
   - For any training point$(\mathbf{x}_i, y_i)$:
    $$ y_i (\mathbf{w}^T \mathbf{x}_i + b) \geq 1$$

3. **Support Vectors**:
   - The optimization problem focuses on the points closest to the decision boundary.
   - The support vectors define the position and orientation of the hyperplane.

### SVM as Constrained Optimization
- **Dual Problem**:
  - By solving the dual form of the optimization problem, we can express the solution in terms of support vectors:
   $$ \mathbf{w} = \sum_{i=1}^{n} \alpha_i y_i \mathbf{x}_i$$
   $$ b = y_k - \mathbf{w}^T \mathbf{x}_k \text{ for any support vector } \mathbf{x}_k$$

- **Classifying Function**:
  - The decision function for classification:
   $$ f(\mathbf{x}) = \sum_{i=1}^{n} \alpha_i y_i \mathbf{x}_i^T \mathbf{x} + b$$

### Non-Linear SVM
1. **Kernel Trick**:
   - For data that is not linearly separable, SVM can use the kernel trick to map data to a higher-dimensional space where it is linearly separable.
   - Common kernel functions:
     - **Polynomial Kernel**:$(\mathbf{x} \cdot \mathbf{y} + c)^d$
     - **Gaussian (RBF) Kernel**:$\exp(-\gamma \|\mathbf{x} - \mathbf{y}\|^2)$
     - **Sigmoid Kernel**:$\tanh(\alpha \mathbf{x} \cdot \mathbf{y} + c)$

2. **Feature Mapping**:
   - Mapping the original feature space to a higher-dimensional space using a kernel function:
    $$ \phi: \mathbf{x} \rightarrow \phi(\mathbf{x})$$

3. **Kernelized SVM**:
   - The optimization problem in the higher-dimensional space is solved using the kernel function without explicitly mapping the data:
    $$ K(\mathbf{x}, \mathbf{y}) = \phi(\mathbf{x})^T \phi(\mathbf{y})$$

### Practical Implementation
- **Using Python and Sklearn**:
  - Implementing SVMs with different kernels using Python's `sklearn.svm.SVC`.

### Summary
- **Linear SVM**:
  - Effective for linearly separable data.
  - Finds the optimal hyperplane by maximizing the margin between classes.

- **Non-Linear SVM**:
  - Uses the kernel trick to handle non-linear separable data.
  - Common kernel functions include polynomial, Gaussian (RBF), and sigmoid.

- **Key Takeaways**:
  - SVMs are powerful for classification tasks, especially in high-dimensional spaces.
  - The kernel trick allows SVMs to handle complex, non-linear decision boundaries.
  - Proper implementation and parameter tuning are crucial for optimal performance.