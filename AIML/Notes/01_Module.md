A# Introduction to AI and Problem Solving Methods
AI enables machines to mimic human problem-solving and reasoning abilities by using logical algorithms and computational intelligence.
- **State-Space Representation**: Represent each possible situation as a "state" and transitions as actions.
- **Problem-Solving Approaches**:
    - **Search-Based**: Explore paths in a state-space (e.g., BFS, DFS).
    - **Optimization-Based**: Focus on finding the optimal solution under given constraints.
    - **Knowledge-Based**: Use rules and logical reasoning to infer solutions.
## Intelligent Agents
An intelligent agent is a computational entity that perceives its environment, decides on actions, and performs tasks to achieve goals.
#### **Types of Intelligent Agents**:

1. **Simple Reflex Agents**: Act only on the current situation (condition-action rules).
2. **Model-Based Reflex Agents**: Maintain internal states to handle partially observable environments.
3. **Goal-Based Agents**: Consider future actions to achieve goals.
4. **Utility-Based Agents**: Aim to maximise utility using a performance measure.
5. **Learning Agents**: Improve their performance based on experience.

#### 2. **How It Works (Logic)**:
Agents interact via the **perception-action loop**:
- **Sensors**: Gather data from the environment.
- **Decision-Making Unit**: Analyse data and choose an action.
- **Actuators**: Perform the chosen action.
#### 4. **How to Build Your Own**:
```python
class ReflexAgent:
    def __init__(self, rules):
        self.rules = rules

    def decide(self, environment):
        return self.rules.get(environment, "do nothing")

# Example: A simple agent
rules = {"enemy seen": "attack", "low health": "retreat"}
agent = ReflexAgent(rules)
print(agent.decide("enemy seen"))  # Output: attack
```
## Different Approaches of AI
#### 1. **Simple Explanation**:
AI can be implemented using three main approaches:

1. **Symbolic AI**: Logic-based, relies on rules and knowledge representation.
2. **Sub-Symbolic AI**: Data-driven, relies on learning patterns (e.g., Neural Networks).
3. **Hybrid AI**: Combines symbolic and sub-symbolic methods.

#### 2. **How It Works (Logic)**:
- Symbolic AI processes information logically through rules and facts.
- Sub-symbolic AI learns representations from data using statistical models.
- Hybrid AI merges logic-based and learning-based reasoning.

#### 3. **How to Use It**:
- Symbolic AI: Use for expert systems and decision trees.
- Sub-symbolic AI: Use for predictions, image recognition, and NLP.

#### 4. **How to Build Your Own**:
- **Symbolic AI**: Write logic and rules using programming.
- **Sub-Symbolic AI**: Train models using machine learning libraries (e.g., TensorFlow).
## Searching Techniques
Searching involves exploring possible solutions systematically to solve problems.
### Uniformed Search
Uninformed search strategies explore the state space without additional knowledge about the goal beyond its definition. They do not use heuristics to guide the search.
Relies solely on exploring nodes systematically, using data structures like queues (BFS) or stacks (DFS).
#### BFS
Explores nodes level by level using a queue.
```python
from collections import deque

def bfs(graph, start, goal):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        visited.add(node)
        queue.extend(n for n in graph[node] if n not in visited)
    return False
```

#### DFS
Explores as far as possible along each branch before backtracking.
```python
def dfs(graph, start, goal, visited=set()):
    if start == goal:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited and dfs(graph, neighbor, goal, visited):
            return True
    return False

```
### Informed Search 
Informed search strategies use heuristics—additional knowledge about the problem—to guide the search towards the goal more efficiently.
Informed searches evaluate the cost to reach the current state and estimate the cost to the goal using a heuristic function.
#### Iterative Deepening
Combines BFS's systematic depth exploration with DFS's depth-first approach
##### How to Implement:

```bash
pip install networkx scipy
```

```python
import networkx as nx

def iterative_deepening_search(graph, start, goal, max_depth=10):
    def dls(node, depth):
        if depth == 0:
            return node == goal
        for neighbor in graph.neighbors(node):
            if dls(neighbor, depth - 1):
                return True
        return False

    for depth in range(max_depth):
        if dls(start, depth):
            return True
    return False

# Create the graph
graph = nx.Graph()
graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('E', 'F')])

print("IDS Result:", iterative_deepening_search(graph, 'A', 'F'))

```
path = nx.bidirectional_shortest_path(graph, 'A', 'F')
print("Bidirectional Search Path:", path)
#### Bidirectional Search
Runs two searches (from the start and goal) and stops when they meet.
> `NetworkX` library has direct function to use this.

```python
path = nx.bidirectional_shortest_path(graph, 'A', 'F')
print("Bidirectional Search Path:", path)
```
### Heuristic Search
Uses a heuristic function to guide the search toward the goal.
Implementing can be done using Priority queue method.

```python
import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_set = [(heuristic[start], start)]
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return True
        visited.add(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic[neighbor], neighbor))
    return False

# Define heuristic
heuristic = {'A': 5, 'B': 4, 'C': 2, 'D': 6, 'E': 1, 'F': 0}
print("Greedy Best-First Result:", greedy_best_first_search(graph, 'A', 'F', heuristic))

```
### Greedy BestFirst Search
Expands the node with the lowest heuristic value.
### A* Search
Combines cost to reach a node and the estimated cost to the goal.
> `NetworkX` also supports direct implementation for A* Search.

```python 
def heuristic_func(node1, node2):
    return heuristic[node1]

path = nx.astar_path(graph, 'A', 'F', heuristic=heuristic_func)
print("A* Search Path:", path)
```

## Uninformed Search vs Informed Search

![Diffrence-Between-Informed&Uninformed](Diffrence-Between-Informed&Uninformed.png)
### Local Search Algorithms
#### Hill Climbing 
Moves toward the highest-valued neighbour until no improvement is possible.
Starts with a random solution and iteratively improves by moving to a neighbouring solution with a better value.

```python
import numpy as np

def hill_climbing(function, start, step_size=0.1, max_iterations=100):
    current = start
    for _ in range(max_iterations):
        neighbors = [current - step_size, current + step_size]
        next_point = max(neighbors, key=function)
        if function(next_point) <= function(current):
            break
        current = next_point
    return current

# Example function: f(x) = -x^2 (maximized at x=0)
result = hill_climbing(lambda x: -x**2, start=2)
print("Hill Climbing Result:", result)
```
#### Simulated Annealing 
Combines randomness to escape local optima with gradual cooling.
Introduces randomness to escape local optima by accepting worse solutions with a probability that decreases over time.

```python
import math
import random

def simulated_annealing(function, start, temp=100, cooling_rate=0.95, min_temp=1e-3):
    current = start
    while temp > min_temp:
        next_point = current + random.uniform(-1, 1)
        delta = function(next_point) - function(current)
        if delta > 0 or math.exp(delta / temp) > random.random():
            current = next_point
        temp *= cooling_rate
    return current

# Example function: f(x) = -x^2
result = simulated_annealing(lambda x: -x**2, start=5)
print("Simulated Annealing Result:", result)
```


![Key Diagram](Diffrence-Between-Hill-&-Simulated.png)
#### Libraries
`SciPy` for optimisation problems:

```python
from scipy.optimize import minimize_scalar

result = minimize_scalar(lambda x: -x**2, bounds=(-10, 10), method='bounded')
print("SciPy Optimization Result:", result.x)
```
`Pyomo` & `OR-Tools` for larger optimisation problems. 
## Adversarial Search
Adversarial Search is used in decision-making scenarios where multiple agents (players) with opposing goals interact, such as in games. The goal is to optimize one's outcome while considering the actions of opponents.
### **Simple Explanation**
- Adversarial search is used in competitive environments like games (e.g., chess, tic-tac-toe).
- The agents take turns, aiming to maximize their own benefits while minimizing the opponent's.
- Typically modeled using a **game tree**, where nodes represent game states and edges represent actions.
### MinMax Algorithms
- Recursively evaluates the game tree, assuming both players play optimally.
- Each node is assigned a value:
    - MAX picks the highest value.
    - MIN picks the lowest value.

```python
def minimax(state, depth, is_maximizing):
    if depth == 0 or is_terminal(state):
        return evaluate(state)

    if is_maximizing:
        max_eval = float('-inf')
        for child in get_children(state):
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(state):
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
```
### Game Playing
- The game is represented as a tree.
- Nodes are game states.
- Edges represent actions leading to new states.
### Aplha-Beta Pruning
Eliminates branches that don't affect the final decision, reducing computation.
```python
def alpha_beta(state, depth, alpha, beta, is_maximizing):
    if depth == 0 or is_terminal(state):
        return evaluate(state)

    if is_maximizing:
        max_eval = float('-inf')
        for child in get_children(state):
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(state):
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
```
### Constrained Satisfaction Problem
A `CSP` is a type of problem where you need to find a solution to a set of variables that must satisfy certain constraints. The objective is to assign values to variables in such a way that all constraints are met.
- **Variables**: Entities that need to be assigned values.
- **Domains**: The set of possible values for each variable.
- **Constraints**: Rules that limit the values that variables can take, often defined in terms of relationships between variables.

**Example**:

- A classic example is the **N-Queens problem**, where you need to place N queens on an NxN chessboard such that no two queens threaten each other. The variables are the positions of the queens, and the constraint is that no two queens should share the same row, column, or diagonal.
#### 3. **How to Use**:
```python
from constraint import Problem

problem = Problem()
problem.addVariable("A", [1, 2, 3])
problem.addVariable("B", [1, 2, 3])
problem.addConstraint(lambda a, b: a != b, ("A", "B"))
print(problem.getSolutions())

```