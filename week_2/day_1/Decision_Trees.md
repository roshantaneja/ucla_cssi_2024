---
tags:
  - lecture
  - notes
  - summer
  - CS
---
## Lecture Notes on Decision Trees

### Outline
1. Motivation
2. Decision Trees
3. Splitting Criteria
4. Stopping Conditions & Pruning
5. Regression Trees
6. Random Forest

### Geometry of Data
- **Logistic Regression**:
  - Works best when classes are well-separated linearly in the feature space and the classification boundary has a “nice geometry”.
  - Decision boundary: 
    $$ \mathbf{w}^T \mathbf{x} + b = 0 $$
  - Sigmoid function:
    $$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

- **Complex Boundaries**:
  - Some data may have well-separated classes, but optimal decision boundaries cannot be easily described by single equations.

### Decision Trees
- **Interpretable Models**:
  - Decision trees are interpretable models that differentiate between classes of objects and phenomena.
- **Properties**:
  1. Interpretable by humans.
  2. Can represent sufficiently complex decision boundaries.
  3. Locally linear decision boundaries, where each component is simple to describe mathematically.

### Tree-based Models
- **Structure**:
  - **Root Node**: The topmost node representing the entire dataset.
  - **Internal Nodes**: Nodes where the data is split based on an attribute.
  - **Leaf Nodes**: Terminal nodes representing class assignments.

### Geometry of Flow Charts
- **Flow Chart Trees**:
  - A flow chart whose graph is a tree (connected and no cycles) represents a decision tree model.
  - Internal nodes represent attributes to test, branching is determined by attribute values, and terminal leaf nodes represent class assignments.

### Learning the Model
- **Training**:
  - Producing an optimal partition of the features with axis-aligned linear boundaries.
  - Each region is predicted to have a class label based on the majority class of the training points in that region.

### Splitting Criteria
- **Guidelines**:
  - Regions should grow progressively purer with splits, specializing towards a single class.
  - Avoid empty regions.

#### How to Define Purity
- **Classification Error**:
  - Measures the impurity of a region:
    $$ E = 1 - \max(p_i) $$
    - Where $p_i$ is the proportion of class $i$ in the region.

- **Entropy**:
  - Quantify the distribution of classes within the region:
    $$ H(p_1, p_2, ..., p_k) = -\sum_{i=1}^k p_i \log_2 p_i $$
    - Where $p_i$ is the proportion of class $i$ in the region.

- **Gini Impurity**:
  - Another measure of impurity:
    $$ G = \sum_{i=1}^k p_i (1 - p_i) $$
    - Where $p_i$ is the proportion of class $i$ in the region.

### Example: Splitting Criteria
- **Attributes to Choose**:
  - Student (Yes/No)
  - Credit Rating (Excellent/Fair)
  - Age (<=30, 31-40, >40)

#### Entropy Calculation Example
- **Formula**:
  $$ H(p_1, p_2, ..., p_k) = -\sum_{i=1}^k p_i \log_2 p_i $$

### Stopping Conditions & Pruning
- **Common Stopping Conditions**:
  - Stop if all instances in the region belong to the same class.
  - Stop if the number of instances in the sub-region falls below a pre-defined threshold (min_samples_leaf).
  - Stop if the total number of leaves in the tree exceeds a pre-defined threshold.

- **Pruning**:
  - Instead of pre-specifying a stopping condition, grow the tree fully and then prune back unnecessary branches.
  - **Cost Complexity Pruning**:
    $$ R_\alpha(T) = R(T) + \alpha |T| $$
    - Where $R(T)$ is the misclassification rate of the tree $T$, and $|T|$ is the number of terminal nodes.

### Regression Trees
- **Adaptations for Regression**:
  - Used for predicting numerical variables.
  - Split criteria based on minimizing variance within each partition.
  - **Mean Squared Error (MSE)**:
    $$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
  - **Mean Absolute Error (MAE)**:
    $$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$

### Random Forest
- **Ensemble Method**:
  - A set of trees (ensemble) used to improve accuracy and reduce overfitting.
  - **Bagging (Bootstrap Aggregating)**:
    - Technique to create multiple subsets of the data and train separate trees on each subset.
    $$ \hat{f}_B(x) = \frac{1}{B} \sum_{b=1}^{B} \hat{f}^{*b}(x) $$
    - Where $B$ is the number of trees and $\hat{f}^{*b}$ is the $b$-th bootstrap sample.

### Summary
- **Classification Trees**:
  - Predict categorical labels using splitting criteria, stopping conditions, and pruning.
- **Regression Trees**:
  - Predict numerical variables.
- **Random Forest**:
  - Ensemble method using bagging to combine multiple decision trees for better performance.