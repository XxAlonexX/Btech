import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000, regularization=None, lambda_param=0.1):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.regularization = regularization
        self.lambda_param = lambda_param
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            
            if self.regularization == 'l1':
                dw = (1/n_samples) * (np.dot(X.T, (y_predicted - y)) + 
                      self.lambda_param * np.sign(self.weights))
            elif self.regularization == 'l2':
                dw = (1/n_samples) * (np.dot(X.T, (y_predicted - y)) + 
                      self.lambda_param * self.weights)
            else:
                dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
                
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
    def score(self, X, y):
        predictions = self.predict(X)
        return 1 - (np.sum((y - predictions) ** 2) / np.sum((y - np.mean(y)) ** 2))

if __name__ == "__main__":
    from sklearn.datasets import make_regression
    from sklearn.model_selection import train_test_split
    
    X, y = make_regression(n_samples=100, n_features=1, noise=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        'No Regularization': LinearRegression(),
        'L1 Regularization': LinearRegression(regularization='l1'),
        'L2 Regularization': LinearRegression(regularization='l2')
    }
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        print(f"{name}:")
        print(f"Training Score: {train_score:.4f}")
        print(f"Testing Score: {test_score:.4f}\n")
