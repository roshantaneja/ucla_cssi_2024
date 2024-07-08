---
tags:
  - notes
  - lecture
  - summer
---
## Lecture Notes on Data Exploration

### Data Science Life Cycle
1. Ask an interesting question
2. Get the Data
3. Explore and Preprocess the Data
4. Model the Data
5. Communicate/Visualize the Results

### Content Overview
1. Vector/Tabular Data
2. Data Exploration: Descriptive Statistics
3. Data Exploration: Data Visualization
4. Data Preprocessing

### Vector/Tabular Data
- **Matrix Representation**:
  - Rows: \( n \) data points
  - Columns: \( p \) features / attributes / dimensions

#### Attribute Types
- **Numerical**: E.g., height, income
- **Categorical/Discrete**:
  - **Nominal**: Categories without order (e.g., hair color)
  - **Binary**: Two categories (e.g., gender, medical test results)
  - **Ordinal**: Ordered categories (e.g., grades, rankings)

### Data Exploration: Descriptive Statistics
1. **Population vs. Sample**:
   - **Population**: Entire set of objects/events under study
   - **Sample**: Representative subset of the population

2. **Biases in Samples**:
   - **Selection Bias**: Certain subjects are more likely to be selected
   - **Volunteer/Nonresponse Bias**: Some subjects are not represented

3. **Basic Statistical Descriptions**:
   - **Central Tendency**: Mean, Median, Mode
   - **Dispersion**: Range, Variance, Standard Deviation, Interquartile Range (IQR)

#### Central Tendency Measures
- **Mean**: 
  $$ \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i $$
- **Median**: Middle value when data is ordered
- **Mode**: Most frequently occurring value

#### Dispersion Measures
- **Range**: Difference between the maximum and minimum values
- **Variance**:
  $$ s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2 $$
- **Standard Deviation**:
  $$ s = \sqrt{s^2} $$
- **Interquartile Range (IQR)**:
  $$ \text{IQR} = Q3 - Q1 $$

### Data Exploration: Data Visualization
1. **Histograms**: Visualize distribution of a single variable
2. **Pie Charts**: Visualize composition of categorical data (often replaced by bar charts)
3. **Scatter Plots**: Visualize relationships between two variables
4. **Scatterplot Matrices**: Multiple scatter plots for higher-dimensional data
5. **Boxplots**: Visualize distribution of quantitative data and identify outliers
6. **Stacked Area Graphs**: Visualize trends over time

#### Visualization Challenges
- **High Dimensionality**: Difficult to plot and interpret many variables
- **Mixed Data Types**: Need conversion schemes for visualization
- **Reducing Complexity**: Use multiple lower-dimensional plots or color coding for better interpretation

### Data Preprocessing
1. **Handling Missing Data**:
   - Drop rows/columns with missing data
   - Replace missing values with mean/median

2. **Handling Outliers**:
   - Identify outliers using definitions (e.g., beyond 1.5 \(\times\) IQR)
   - Drop rows with outliers

3. **Feature Preparation**:
   - Define features (\(X\)) and labels (\(y\))
   - Add new features (e.g., living area per bed)
   - Transform categorical features to numerical values using one-hot encoding or binary encoding

4. **Feature Normalization**:
   - **Z-score Normalization**: Transform to have mean 0 and standard deviation 1
   - **Min-max Normalization**: Scale values to a range [0, 1]

### Summary
- **Explore vector/tabular data**
- **Attribute types**
- **Basic statistics**
- **Visualization techniques**
- **Data Preprocessing methods**

### Today's Lab
- Get familiar with BruinLearn, Piazza, GradeScope
- Review Python libraries for data science (Numpy, Pandas, Matplotlib)
- Practice data exploration and preprocessing (e.g., `read_csv`, `drop`)
- Help with  [Homework 0](80_Learning_Education/82_Summer_Courses/82.30_ucla_cssi_2024/homework/homework_0/homework_0.md)
- 