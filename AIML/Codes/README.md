# AI Algorithms Implementation

A comprehensive collection of AI algorithms implemented in Python.

## Directory Structure
```
Codes/
├── search/
│   ├── graph_search.py    # DFS, BFS, Iterative Deepening, Bidirectional Search
│   ├── informed_search.py # A*, Greedy Best-First Search
│   ├── local_search.py    # Hill Climbing, Simulated Annealing
│   └── csp.py            # Constraint Satisfaction Problems
├── games/
│   └── minimax.py        # Minimax, Alpha-Beta Pruning
└── agents/
    └── agent.py          # Intelligent Agent Framework
```

## Algorithms and Libraries Used

### Search Algorithms (`search/`)
- [graph_search.py](search/graph_search.py)
  - Libraries: `collections` (deque, defaultdict)
  - Algorithms: 
    - Depth-First Search (DFS)
    - Breadth-First Search (BFS)
    - Iterative Deepening Search
    - Bidirectional Search

- [informed_search.py](search/informed_search.py)
  - Libraries: `heapq`, `math`
  - Algorithms: 
    - A* Search
    - Greedy Best-First Search
  - Heuristics: Manhattan Distance, Euclidean Distance

- [local_search.py](search/local_search.py)
  - Libraries: `random`, `math`
  - Algorithms:
    - Hill Climbing
    - Simulated Annealing

- [csp.py](search/csp.py)
  - Pure Python implementation
  - Algorithms:
    - Backtracking Search
    - Forward Checking
    - Map Coloring Example

### Game Theory (`games/`)
- [minimax.py](games/minimax.py)
  - Pure Python implementation
  - Algorithms:
    - Minimax Algorithm
    - Alpha-Beta Pruning
    - Best Move Selection

### Intelligent Agents (`agents/`)
- [agent.py](agents/agent.py)
  - Pure Python implementation
  - Agent Types:
    - Reflex Agent
    - Model-Based Agent
    - Goal-Based Agent
    - Environment Class

## Dependencies
All implementations use Python's standard library only:
- collections
- heapq
- math
- random


## Usage Examples
> Simple use of algorithms:
### Using Graph Search Algorithms
```python
from search.graph_search import Graph

# Create a graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')

# Find path using DFS
path = g.dfs('A', 'C')
```

### Using A* Search
```python
from search.informed_search import astar_search

# Define your heuristic function
def my_heuristic(state, goal):
    return manhattan_distance(state, goal)

# Use A* search
path = astar_search(start_state, goal_state, get_neighbors, my_heuristic)
```

### Using Minimax for Games
```python
from games.minimax import get_best_move

# Get best move using alpha-beta pruning
best_move = get_best_move(game_state, depth=3, get_moves=get_valid_moves, 
                         evaluate=evaluate_position)
```

### Creating an Intelligent Agent
```python
from agents.agent import ReflexAgent

# Create a reflex agent with rules
agent = ReflexAgent(rules=[
    (lambda state: state.danger, lambda: 'escape'),
    (lambda state: state.food_nearby, lambda: 'eat')
])
