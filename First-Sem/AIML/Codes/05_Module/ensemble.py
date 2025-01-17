import numpy as np
from collections import Counter

class SimpleEnsemble:
    def __init__(self, n_models=5):
        self.n_models = n_models
        self.models = []
        
    def _bootstrap_sample(self, X, y):
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, size=n_samples, replace=True)
        return X[indices], y[indices]
    
    def fit(self, X, y):
        self.models = []
        for _ in range(self.n_models):
            X_boot, y_boot = self._bootstrap_sample(X, y)
            model = WeakLearner()
            model.fit(X_boot, y_boot)
            self.models.append(model)
    
    def predict(self, X):
        predictions = np.array([model.predict(X) for model in self.models])
        return np.array([Counter(pred).most_common(1)[0][0] for pred in predictions.T])

class WeakLearner:
    def fit(self, X, y):
        self.X = X
        self.y = y
        
    def predict(self, X):
        predictions = []
        for x in X:
            # Simple nearest neighbor prediction
            distances = np.sum((self.X - x) ** 2, axis=1)
            nearest_idx = np.argmin(distances)
            predictions.append(self.y[nearest_idx])
        return np.array(predictions)

# Example usage
if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
    y = np.array([0, 0, 0, 1, 1])
    
    ensemble = SimpleEnsemble(n_models=3)
    ensemble.fit(X, y)
    print("Predictions:", ensemble.predict([[2, 3], [6, 7]]))