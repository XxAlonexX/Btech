import numpy as np
from scipy.spatial.distance import pdist, squareform

class AgglomerativeClustering:
    def __init__(self, n_clusters=2, linkage='single'):
        self.n_clusters = n_clusters
        self.linkage = linkage
    
    def _get_distance(self, cluster1, cluster2):
        distances = self.distance_matrix[np.ix_(cluster1, cluster2)]
        if self.linkage == 'single':
            return np.min(distances)
        elif self.linkage == 'complete':
            return np.max(distances)
        else:  # average
            return np.mean(distances)
    
    def fit(self, X):
        n_samples = X.shape[0]
        self.labels_ = np.arange(n_samples)
        
        self.distance_matrix = squareform(pdist(X))
        current_clusters = [{i} for i in range(n_samples)]
        
        while len(current_clusters) > self.n_clusters:
            min_dist = float('inf')
            merge_i, merge_j = 0, 0
            
            for i in range(len(current_clusters)):
                for j in range(i + 1, len(current_clusters)):
                    dist = self._get_distance(list(current_clusters[i]), 
                                           list(current_clusters[j]))
                    if dist < min_dist:
                        min_dist = dist
                        merge_i, merge_j = i, j
            
            new_cluster = current_clusters[merge_i].union(current_clusters[merge_j])
            label = min(self.labels_[list(new_cluster)])
            for idx in new_cluster:
                self.labels_[idx] = label
                
            current_clusters = [current_clusters[i] for i in range(len(current_clusters))
                              if i not in [merge_i, merge_j]]
            current_clusters.append(new_cluster)
        
        return self

if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=0)
    
    agnes = AgglomerativeClustering(n_clusters=3, linkage='single')
    agnes.fit(X)
    print("Cluster Labels:", np.unique(agnes.labels_))
