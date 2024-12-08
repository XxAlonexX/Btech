import numpy as np
from sklearn.neighbors import NearestNeighbors

class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
    
    def fit(self, X):
        self.labels_ = np.full(X.shape[0], -1)
        neighbors = NearestNeighbors(radius=self.eps).fit(X)
        distances, indices = neighbors.radius_neighbors(X)
        
        cluster_label = 0
        for i in range(X.shape[0]):
            if self.labels_[i] != -1:
                continue
                
            if len(indices[i]) >= self.min_samples:
                self._expand_cluster(i, indices[i], cluster_label, indices)
                cluster_label += 1
        
        return self
    
    def _expand_cluster(self, point_idx, neighbors, cluster_label, all_neighbors):
        self.labels_[point_idx] = cluster_label
        
        i = 0
        while i < len(neighbors):
            point = neighbors[i]
            if self.labels_[point] == -1:
                self.labels_[point] = cluster_label
                if len(all_neighbors[point]) >= self.min_samples:
                    neighbors = np.append(neighbors, all_neighbors[point])
            i += 1

if __name__ == "__main__":
    from sklearn.datasets import make_moons
    X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)
    
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    dbscan.fit(X)
    print("Number of clusters:", len(np.unique(dbscan.labels_[dbscan.labels_ >= 0])))
