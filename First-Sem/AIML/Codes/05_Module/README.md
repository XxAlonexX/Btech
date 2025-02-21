# Probabilistic and Reinforcement Learning Implementations

This module contains implementations of various probabilistic learning algorithms, reinforcement learning, and ensemble methods.

## Algorithms Implemented

### 1. [Naive Bayes Classifier](./naive_bayes.py)
- Probabilistic classifier based on Bayes' theorem
- Features:
  - Gaussian Naive Bayes implementation
  - Handles continuous features
  - Calculates class and feature probabilities
  - Uses log probabilities for numerical stability

### 2. [Q-Learning](./q_learning.py)
- Simple Q-Learning implementation for reinforcement learning
- Features:
  - Customizable learning rate and discount factor
  - Epsilon-greedy action selection
  - Q-table based value function
  - Supports arbitrary state and action spaces

### 3. [Ensemble Learning](./ensemble.py)
- Basic ensemble learning implementation
- Features:
  - Bootstrap sampling (Bagging)
  - Weak learner implementation
  - Majority voting for predictions
  - Simple nearest neighbor base classifier

## Dependencies
- NumPy
- Collections (Python standard library)

## Usage Examples

### Naive Bayes
```python
from naive_bayes import NaiveBayes
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y = np.array([0, 0, 0, 1, 1])

nb = NaiveBayes()
nb.fit(X, y)
predictions = nb.predict([[2, 3], [6, 7]])
```

### Q-Learning
```python
from q_learning import QLearning

agent = QLearning(n_states=4, n_actions=4)
# Training loop
state = 0
action = agent.choose_action(state)
next_state = 1  # From environment
reward = 1      # From environment
agent.learn(state, action, reward, next_state)
```

### Ensemble Learning
```python
from ensemble import SimpleEnsemble
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y = np.array([0, 0, 0, 1, 1])

ensemble = SimpleEnsemble(n_models=3)
ensemble.fit(X, y)
predictions = ensemble.predict([[2, 3], [6, 7]])
```

## Implementation Details

1. **Naive Bayes**
   - Uses Gaussian probability distribution
   - Handles numerical features
   - Calculates class probabilities and feature likelihoods

2. **Q-Learning**
   - Implements basic Q-learning algorithm
   - Uses epsilon-greedy exploration strategy
   - Maintains Q-table for state-action values

3. **Ensemble Learning**
   - Implements bagging ensemble method
   - Uses bootstrap sampling
   - Simple majority voting for final predictions

Each implementation focuses on clarity and simplicity while maintaining core functionality.
