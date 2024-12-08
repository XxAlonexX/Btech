# Clustering Algorithms Implementation

This module contains implementations of various clustering algorithms using NumPy and SciPy.

## Algorithms Implemented

### 1. [K-Means](./kmeans.py)
- Centroid-based clustering
- Uses Euclidean distance
- Minimizes within-cluster variance

### 2. [K-Modes](./kmodes.py)
- For categorical data
- Uses hamming distance
- Mode-based centroids

### 3. [K-Medians](./kmedians.py)
- Similar to K-means
- Uses Manhattan distance
- Median-based centroids

### 4. [Hierarchical Clustering (AGNES)](./hierarchical.py)
- Agglomerative clustering
- Supports different linkage methods
- Bottom-up approach

### 5. [DBSCAN](./dbscan.py)
- Density-based clustering
- Handles non-spherical clusters
- Noise point detection

### 6. [Gaussian Mixture Model](./gmm.py)
- Probabilistic clustering
- EM algorithm implementation
- Soft clustering assignments

## Dependencies
- NumPy
- SciPy
- scikit-learn (for some utility functions and example datasets)

## Usage Examples

### K-Means
```python
from kmeans import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.predict(X_new)
```

### DBSCAN
```python
from dbscan import DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X)
labels = dbscan.labels_
```

### Gaussian Mixture
```python
from gmm import GaussianMixture
gmm = GaussianMixture(n_components=3)
gmm.fit(X)
labels = gmm.predict(X_new)
```

## Implementation Details

Each algorithm is implemented with focus on:
- Simplicity and readability
- Efficient NumPy operations
- Standard clustering interface
- Example usage with sklearn datasets
