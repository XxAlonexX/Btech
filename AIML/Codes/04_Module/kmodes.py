import numpy as np
from collections import Counter

class KModes:
    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
    
    def _mode(self, X):
        if len(X) == 0:
            return self.centroids[0]
        return np.array([Counter(X[:, i]).most_common(1)[0][0] for i in range(X.shape[1])])
    
    def _dissimilarity(self, X, Y):
        return np.sum(X != Y, axis=1)
    
    def fit(self, X):
        n_samples = X.shape[0]
        self.centroids = X[np.random.choice(n_samples, self.n_clusters, replace=False)]
        
        for _ in range(self.max_iters):
            old_centroids = self.centroids.copy()
            distances = np.array([self._dissimilarity(X, centroid) for centroid in self.centroids])
            self.labels = np.argmin(distances, axis=0)
            
            for k in range(self.n_clusters):
                if sum(self.labels == k) > 0:
                    self.centroids[k] = self._mode(X[self.labels == k])
            
            if np.all(old_centroids == self.centroids):
                break
        return self
    
    def predict(self, X):
        distances = np.array([self._dissimilarity(X, centroid) for centroid in self.centroids])
        return np.argmin(distances, axis=0)

if __name__ == "__main__":
    X = np.array([
        ['a', 'b', 'c'],
        ['a', 'b', 'd'],
        ['d', 'e', 'f'],
        ['d', 'e', 'g']
    ])
    
    kmodes = KModes(n_clusters=2)
    kmodes.fit(X)
    print("Labels:", kmodes.labels)
