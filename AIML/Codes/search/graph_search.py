from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start, goal):
        visited = set()
        stack = [(start, [start])]
        
        while stack:
            vertex, path = stack.pop()
            if vertex == goal:
                return path
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return []
    
    def bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])
        
        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return []
    
    def iterative_deepening(self, start, goal, max_depth):
        def dls(node, goal, depth, path):
            if depth == 0 and node == goal:
                return path
            if depth > 0:
                for neighbor in self.graph[node]:
                    result = dls(neighbor, goal, depth - 1, path + [neighbor])
                    if result:
                        return result
            return None
        
        for depth in range(max_depth):
            result = dls(start, goal, depth, [start])
            if result:
                return result
        return []
    
    def bidirectional_search(self, start, goal):
        if start == goal:
            return [start]
            
        forward_queue = deque([(start, [start])])
        backward_queue = deque([(goal, [goal])])
        forward_visited = {start: [start]}
        backward_visited = {goal: [goal]}
        
        while forward_queue and backward_queue:
            current, path = forward_queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor in backward_visited:
                    return path + backward_visited[neighbor][::-1][1:]
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = path + [neighbor]
                    forward_queue.append((neighbor, path + [neighbor]))
            
            current, path = backward_queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor in forward_visited:
                    return forward_visited[neighbor] + path[::-1][1:]
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = path + [neighbor]
                    backward_queue.append((neighbor, path + [neighbor]))
        return []
