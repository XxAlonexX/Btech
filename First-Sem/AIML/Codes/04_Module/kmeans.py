import numpy as np

class KMeans:
    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        
    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        
        for _ in range(self.max_iters):
            old_centroids = self.centroids.copy()
            distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
            self.labels = np.argmin(distances, axis=0)
            
            for k in range(self.n_clusters):
                if sum(self.labels == k) > 0:
                    self.centroids[k] = X[self.labels == k].mean(axis=0)
                    
            if np.all(old_centroids == self.centroids):
                break
                
        self.inertia_ = np.sum((X - self.centroids[self.labels])**2)
        return self

    def predict(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
    
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)
    print("Inertia:", kmeans.inertia_)
