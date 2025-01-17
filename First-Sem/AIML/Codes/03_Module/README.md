# Machine Learning Algorithms Implementation

This module contains implementations of fundamental machine learning algorithms from scratch using NumPy.

## Algorithms Implemented

### 1. [Linear Regression](./linear_regression.py)
- Basic linear regression implementation
- L1 (Lasso) regularization
- L2 (Ridge) regularization
- Includes training and testing score calculations

### 2. [Logistic Regression](./logistic_regression.py)
- Binary classification implementation
- Sigmoid activation function
- Gradient descent optimization
- Accuracy metrics

### 3. [Decision Tree](./decision_tree.py)
- Classification tree implementation
- Information gain splitting criterion
- Entropy calculations
- Recursive tree building
- Supports max depth and min samples split parameters

## Dependencies
- NumPy
- sklearn (only for generating sample datasets in examples)

## Usage Examples

### Linear Regression
```python
from linear_regression import LinearRegression

# Create and train model with L2 regularization
model = LinearRegression(regularization='l2', lambda_param=0.1)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Logistic Regression
```python
from logistic_regression import LogisticRegression

# Create and train model
model = LogisticRegression(learning_rate=0.01, n_iterations=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Decision Tree
```python
from decision_tree import DecisionTree

# Create and train model
tree = DecisionTree(max_depth=5, min_samples_split=2)
tree.fit(X_train, y_train)
predictions = tree.predict(X_test)
```

## Implementation Details

Each algorithm is implemented with the following considerations:

1. **Linear Regression**
   - Supports both L1 and L2 regularization
   - Uses gradient descent optimization
   - Includes R² score calculation

2. **Logistic Regression**
   - Binary classification using sigmoid function
   - Gradient descent optimization
   - Accuracy metric implementation

3. **Decision Tree**
   - Information gain criterion for splitting
   - Recursive tree building
   - Support for max depth and min samples split
   - Node class for tree structure
