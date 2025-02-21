import numpy as np
from scipy.stats import multivariate_normal

class GaussianMixture:
    def __init__(self, n_components=3, max_iters=100, tol=1e-3):
        self.n_components = n_components
        self.max_iters = max_iters
        self.tol = tol
        
    def _initialize(self, X):
        n_samples, n_features = X.shape
        
        self.weights_ = np.ones(self.n_components) / self.n_components
        self.means_ = X[np.random.choice(n_samples, self.n_components, replace=False)]
        self.covs_ = [np.eye(n_features) for _ in range(self.n_components)]
        
    def fit(self, X):
        self._initialize(X)
        
        for _ in range(self.max_iters):
            # E-step
            resp = self._e_step(X)
            
            # M-step
            weights_old = self.weights_.copy()
            self._m_step(X, resp)
            
            if np.allclose(weights_old, self.weights_, rtol=self.tol):
                break
                
        return self
    
    def _e_step(self, X):
        resp = np.zeros((X.shape[0], self.n_components))
        
        for k in range(self.n_components):
            resp[:, k] = self.weights_[k] * multivariate_normal.pdf(X, 
                mean=self.means_[k], cov=self.covs_[k])
            
        resp /= resp.sum(axis=1, keepdims=True)
        return resp
    
    def _m_step(self, X, resp):
        N = resp.sum(axis=0)
        self.weights_ = N / X.shape[0]
        
        for k in range(self.n_components):
            self.means_[k] = X.T @ resp[:, k] / N[k]
            diff = X - self.means_[k]
            self.covs_[k] = (diff.T @ (diff * resp[:, k, np.newaxis])) / N[k]
    
    def predict(self, X):
        resp = self._e_step(X)
        return resp.argmax(axis=1)

if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=0)
    
    gmm = GaussianMixture(n_components=3)
    gmm.fit(X)
    labels = gmm.predict(X)
    print("Number of samples in each cluster:", np.bincount(labels))
