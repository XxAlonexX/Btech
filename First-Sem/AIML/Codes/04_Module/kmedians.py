import numpy as np

class KMedians:
    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
    
    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        
        for _ in range(self.max_iters):
            old_centroids = self.centroids.copy()
            distances = np.abs(X - self.centroids[:, np.newaxis]).sum(axis=2)
            self.labels = np.argmin(distances, axis=0)
            
            for k in range(self.n_clusters):
                if sum(self.labels == k) > 0:
                    self.centroids[k] = np.median(X[self.labels == k], axis=0)
            
            if np.all(old_centroids == self.centroids):
                break
                
        self.inertia_ = np.sum(np.abs(X - self.centroids[self.labels]))
        return self
    
    def predict(self, X):
        distances = np.abs(X - self.centroids[:, np.newaxis]).sum(axis=2)
        return np.argmin(distances, axis=0)

if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
    
    kmedians = KMedians(n_clusters=4)
    kmedians.fit(X)
    print("Inertia:", kmedians.inertia_)
