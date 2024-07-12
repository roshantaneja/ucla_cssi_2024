---
tags:
  - lecture
  - notes
  - summer
---
## Lecture Notes on Clustering Basics Presentation

## Announcements
- **Homework 4**: Due tonight at 10 pm
- **Project's First Idea Implementation**: Check-in with TA (5% of grade)
- **Research Seminar**: Next Monday, 1 pm - 2:30 pm, Boelter Hall 3400
  - Speaker: Prof. Jason Cong
  - Topic: Automating Chip Designs and Quantum Computing
- **Midterm Exam**: Next Tuesday, 1:00 pm - 3:00 pm, Boelter Hall 3400
  - Topics: Everything up to clustering
  - Cheat Sheet: Letter size, double-sided, hand-written
  - Calculator: Simple calculators only
  - Question Types: T/F, multiple choice, writing/calculation

---

## Outline
1. Clustering Analysis: Basic Concepts
2. K-means
3. Hierarchical Methods
4. DBSCAN
5. Summary

---

## Supervised vs. Unsupervised Learning
- **Supervised Learning**: Dataset of pairs $(\mathbf{x}_i, y_i)$, with a predictive model $\hat{y} = f(\mathbf{x})$. Adjust model parameters using the average loss over the dataset.
- **Unsupervised Learning**: No target values $y$. Learn inherent data structure. Focus on clustering to group data points automatically.

---

## What is Cluster Analysis?
- **Cluster**: Collection of data objects similar to one another within the same group and dissimilar to objects in other groups.
- **Cluster Analysis (Clustering)**: Finding similarities between data based on characteristics and grouping similar objects into clusters.

### Applications
- Data reduction
- Summarization (preprocessing for regression, classification, association analysis)
- Compression (image processing)
- Prediction based on groups
- Finding K-nearest Neighbors
- Outlier detection

### Examples
- Biology: Taxonomy of living things
- Information retrieval: Document clustering
- Marketing: Discovering distinct customer groups
- City-planning: Identifying house groups by type, value, location
- Earthquake studies: Clustering earthquake epicenters
- Climate: Finding patterns in atmospheric and ocean data
- Finance: Volatility clustering for stock trading days

---

## Partitioning Methods

### Partition Definition
- Divide space into different portions, detect local structures of data.

### Steps
1. **Initial Partitioning**: Randomly assign data points to clusters.
2. **Quality Measure**: Use a measure to determine if the partition is good (e.g., sum of squared distances between data points and cluster centers).

### K-means Objective
- Minimize sum of squared distances between data points and cluster centroids.

---

## K-means Clustering Method
1. Randomly assign $k$ seed points as cluster centroids.
2. Assign each data point to the nearest centroid.
3. Compute new centroids of current partitioning.
4. Repeat steps 2-3 until assignments do not change.

### Example
- Image Segmentation
- Brain Scan Analysis

### Hyperparameter
- Number of clusters $k$

---

## Hierarchical Clustering

### Distance Measures
- **Closest point (single linkage)**
- **Farthest point (complete linkage)**
- **Average of all points (average linkage)**

### Methods
1. **Bottom-up (Agglomerative)**: Start with individual points as clusters, merge closest clusters iteratively.
2. **Top-down (Divisive)**: Start with one cluster, split into smaller clusters iteratively.

### Steps
1. Initialization: Place each data point in its own cluster.
2. Merge closest clusters.
3. Update distance matrix.
4. Repeat until all data points are in a single cluster or desired number of clusters is reached.

### Linkage Types
- **Single Linkage**: Tendency to form long chains.
- **Complete Linkage**: Sensitive to outliers.
- **Average Linkage**: Compromise between single and complete linkage.

---

## Density-Based Clustering Methods (DBSCAN)
- **Density-based Clustering**: Clustering based on density, discovering clusters of arbitrary shape, handling noise.
- **Parameters**:
  - $\epsilon$: Maximum radius of the neighborhood.
  - $\text{MinPts}$: Minimum number of points in $\epsilon$-neighborhood.
  
### Concepts
- **Core Point**: A point with at least \(\text{MinPts}\) within $\epsilon$-neighborhood.
- **Directly Density-Reachable**: Point $p$ is directly density-reachable from point $q$ if $q$ is a core point and $p$ is within $\epsilon$-neighborhood of $q$.
- **Density-Reachable**: Chain of directly density-reachable points.
- **Density-Connected**: Two points $p$ and $q$ are density-connected if there is a point $o$ such that both $p$ and $q$ are density-reachable from $o$.

### DBSCAN Algorithm
1. Start with an arbitrary point.
2. Retrieve all points density-reachable from the starting point.
3. If the starting point is a core point, form a cluster.
4. If not, mark it as noise.
5. Repeat for remaining points.

### Features
- Handles noise.
- Finds clusters of arbitrary shape.

---

## Summary
- Cluster analysis groups objects based on similarity with wide applications.
- K-means: Popular partitioning-based clustering algorithm.
- Hierarchical clustering: Builds a tree of clusters.
- DBSCAN: Density-based algorithm suitable for clusters of arbitrary shape.

---

### Further References
- Research papers on clustering methods and applications.
- Visual tools and examples for understanding clustering algorithms.

---

This concludes the notes on clustering basics from the presentation.