# Unsupervised Machine Learning
Unsupervised learning involves learning from data that has no labeled outcomes. The system tries to identify patterns and structure from the input data without any guidance or predefined labels. The primary goal is to explore the underlying structure or distribution in the data.

---
# Introduction to Clustering 
**Clustering** is a type of unsupervised learning where the goal is to group similar data points together. Each group formed is called a **cluster**, and the data points in the same cluster are more similar to each other than to those in other clusters.

Clustering is widely used in applications like customer segmentation, anomaly detection, and pattern recognition.
## Types of Clustering 
There are various types of clustering methods, and the main ones include:

1. **Partitioning Clustering**: Divides the data into non-overlapping subsets (clusters).
    
    - Example: **K-Means**, **K-Medoids**.
2. **Hierarchical Clustering**: Creates a tree-like structure of clusters, where clusters are merged or divided based on a distance metric.
    
    - Example: **AGNES**, **DIANA**.
3. **Density-Based Clustering**: Identifies clusters based on the density of data points in a region.
    
    - Example: **DBSCAN**.
### K-Means Clustering 
**K-Means** is one of the most popular clustering algorithms. It partitions the data into `K` clusters. The algorithm assigns each data point to the nearest cluster based on the distance to the cluster centroids (mean).

**How it works**:

1. Initialize `K` cluster centroids randomly.
2. Assign each data point to the nearest centroid.
3. Recompute the centroids by averaging the points in each cluster.
4. Repeat steps 2 and 3 until convergence (centroids do not change).
 
**Formula**: The objective is to minimize the **within-cluster sum of squares (WCSS)**:
![K-Means](K-Means.png)

**Implementation**
```python 
from sklearn.cluster import KMeans
import numpy as np

# Sample Data
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Get the cluster labels
labels = kmeans.labels_
print(f'Cluster labels: {labels}')

# Get the cluster centers
centers = kmeans.cluster_centers_
print(f'Cluster centers: {centers}')
```

### K-Mode
**K-Mode Clustering** is a variation of K-Means, specifically for categorical data. Instead of computing the mean, K-Mode uses the mode (most frequent value) for each feature.

**How it works**:

1. Initialize `K` cluster modes randomly.
2. Assign each data point to the nearest mode (mode-based distance).
3. Recompute the modes of the clusters.
4. Repeat steps until convergence.
### K-Medoid
**K-Medoids** is similar to K-Means, but instead of using the mean of data points as the centroid, it selects actual data points as the centers of clusters. This makes it more robust to outliers than K-Means.

**How it works**:

1. Initialize `K` medoids randomly.
2. Assign each point to the closest medoid.
3. Recompute the medoids by choosing the point that minimizes the sum of distances to all other points in the cluster.
4. Repeat until convergence.
### Hierarchical Clustering 
Hierarchical clustering creates a **tree-like structure** of clusters called a **dendrogram**. There are two main types:

- **Agglomerative (AGNES)**: Bottom-up approach where each data point starts in its own cluster, and pairs of clusters are merged as you move up the tree.
- **Divisive (DIANA)**: Top-down approach where all points start in one cluster and are divided into smaller clusters as you move down the tree.
### Density Based Clustering
**Density-Based Spatial Clustering of Applications with Noise (DBSCAN)** is a clustering algorithm that groups data points that are closely packed together, marking points in low-density regions as outliers.

**How it works**:

1. A point is a **core point** if it has more than `MinPts` points within a specified radius (`epsilon`).
2. **Density-reachable** points are points that can be reached from a core point by following a chain of core points.
3. Points that are not core points and cannot be reached by core points are considered **noise**.

DBSCAN does not require the number of clusters to be specified and can find arbitrarily shaped clusters.

---
### Single-Linkage
These are methods used to calculate the distance between clusters in **hierarchical clustering**.

- **Single-Linkage**: The distance between two clusters is defined as the shortest distance between any two points, one from each cluster.
### Multiple Linkage 
   
- **Complete-Linkage (Multiple-Linkage)**: The distance between two clusters is defined as the longest distance between any two points, one from each cluster.
---
### AGNES Algorithm
**AGglomerative NESting (AGNES)** is an agglomerative hierarchical clustering method. It starts with each point as its own cluster and merges the closest clusters iteratively.

**How it works**:

1. Start with `N` clusters (one for each point).
2. At each step, merge the two clusters that are closest according to a chosen distance metric.
3. Continue until only one cluster remains or a stopping condition is met.
### DIANA Algorithm
**DIvisive ANAlysis (DIANA)** is a divisive hierarchical clustering method. It starts with all points in one cluster and recursively divides them into smaller clusters.

**How it works**:

1. Start with all data points in a single cluster.
2. Recursively split the cluster that is most dissimilar to others into two.
3. Continue splitting until a stopping condition is met.

---
### Gaussian Mixture Model
**Gaussian Mixture Model (GMM)** is a probabilistic model for clustering, where data points are modeled as a mixture of multiple Gaussian distributions. Each cluster is represented by a Gaussian distribution.

**How it works**:

1. Each data point is assigned a probability of belonging to each cluster.
2. GMM uses the **Expectation-Maximization (EM)** algorithm to estimate the parameters (mean, covariance, and weight) of the Gaussian distributions iteratively.

---
### DBSCAN
**DBSCAN** is a density-based clustering algorithm that groups closely packed points and marks points in low-density regions as outliers. It requires two parameters: the radius (`epsilon`) and the minimum number of points required (`MinPts`) to form a cluster.

**How it works**:

1. For each point, check if it has at least `MinPts` points within a radius of `epsilon`.
2. Core points with sufficient neighbors form clusters.
3. Points that are reachable from core points are assigned to the same cluster.
4. Points not reachable from any core point are classified as noise.