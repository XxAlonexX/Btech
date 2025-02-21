import numpy as np

class QLearning:
    def __init__(self, n_states, n_actions, learning_rate=0.1, discount_factor=0.95):
        self.q_table = np.zeros((n_states, n_actions))
        self.lr = learning_rate
        self.gamma = discount_factor
        
    def choose_action(self, state, epsilon=0.1):
        if np.random.random() < epsilon:
            return np.random.randint(self.q_table.shape[1])
        return np.argmax(self.q_table[state])
    
    def learn(self, state, action, reward, next_state):
        old_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        
        new_value = (1 - self.lr) * old_value + self.lr * (reward + self.gamma * next_max)
        self.q_table[state, action] = new_value

# Example usage
if __name__ == "__main__":
    # Simple grid world environment (4 states, 4 actions)
    agent = QLearning(n_states=4, n_actions=4)
    
    # Training loop
    for episode in range(100):
        state = 0  # Start state
        for step in range(10):
            action = agent.choose_action(state)
            # Simulate environment (simplified)
            next_state = (state + action) % 4
            reward = 1 if next_state == 3 else 0
            
            agent.learn(state, action, reward, next_state)
            state = next_state
            
            if next_state == 3:  # Goal state
                break
    
    print("Q-Table after training:\n", agent.q_table)