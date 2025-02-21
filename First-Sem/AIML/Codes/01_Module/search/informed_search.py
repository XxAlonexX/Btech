import heapq
from math import sqrt

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def euclidean_distance(p1, p2):
    return sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

def manhattan_distance(p1, p2):
    return sum(abs(x - y) for x, y in zip(p1, p2))

def astar_search(start, goal, get_neighbors, heuristic=manhattan_distance):
    frontier = []
    heapq.heappush(frontier, Node(start, None, 0, heuristic(start, goal)))
    explored = set()
    
    while frontier:
        current = heapq.heappop(frontier)
        
        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]
            
        explored.add(current.state)
        
        for next_state, step_cost in get_neighbors(current.state):
            if next_state not in explored:
                new_cost = current.cost + step_cost
                new_node = Node(next_state, current, new_cost, 
                              heuristic(next_state, goal))
                heapq.heappush(frontier, new_node)
    return None

def greedy_best_first_search(start, goal, get_neighbors, heuristic=manhattan_distance):
    frontier = []
    heapq.heappush(frontier, Node(start, None, 0, heuristic(start, goal)))
    explored = set()
    
    while frontier:
        current = heapq.heappop(frontier)
        
        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]
            
        explored.add(current.state)
        
        for next_state, _ in get_neighbors(current.state):
            if next_state not in explored:
                new_node = Node(next_state, current, 0, 
                              heuristic(next_state, goal))
                heapq.heappush(frontier, new_node)
