import numpy as np
from collections import defaultdict

class NaiveBayes:
    def __init__(self):
        self.class_probs = {}
        self.feature_probs = defaultdict(lambda: defaultdict(dict))
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        classes = np.unique(y)
        
        # Calculate class probabilities
        for c in classes:
            self.class_probs[c] = np.mean(y == c)
            
        # Calculate feature probabilities for each class
        for c in classes:
            class_samples = X[y == c]
            for feature in range(n_features):
                mean = np.mean(class_samples[:, feature])
                std = np.std(class_samples[:, feature]) + 1e-6
                self.feature_probs[c][feature] = {'mean': mean, 'std': std}
    
    def _gaussian_pdf(self, x, mean, std):
        exponent = -((x - mean) ** 2) / (2 * std ** 2)
        return np.exp(exponent) / (std * np.sqrt(2 * np.pi))
    
    def predict(self, X):
        predictions = []
        for x in X:
            class_scores = {}
            for c in self.class_probs:
                score = np.log(self.class_probs[c])
                for feature, value in enumerate(x):
                    params = self.feature_probs[c][feature]
                    score += np.log(self._gaussian_pdf(value, params['mean'], params['std']))
                class_scores[c] = score
            predictions.append(max(class_scores, key=class_scores.get))
        return np.array(predictions)

# Example usage
if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
    y = np.array([0, 0, 0, 1, 1])
    
    nb = NaiveBayes()
    nb.fit(X, y)
    print("Predictions:", nb.predict([[2, 3], [6, 7]]))