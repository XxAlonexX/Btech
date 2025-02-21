import random
import math

def hill_climbing(initial_state, get_neighbors, evaluate):
    current = initial_state
    current_value = evaluate(current)
    
    while True:
        neighbors = get_neighbors(current)
        if not neighbors:
            return current
            
        neighbor_values = [(n, evaluate(n)) for n in neighbors]
        best_neighbor, best_value = max(neighbor_values, key=lambda x: x[1])
        
        if best_value <= current_value:
            return current
            
        current = best_neighbor
        current_value = best_value

def simulated_annealing(initial_state, get_neighbors, evaluate, temp=1000.0, 
                       cooling_rate=0.95, min_temp=1e-10):
    current = initial_state
    current_value = evaluate(current)
    best = current
    best_value = current_value
    temperature = temp
    
    while temperature > min_temp:
        neighbors = get_neighbors(current)
        if not neighbors:
            break
            
        next_state = random.choice(neighbors)
        next_value = evaluate(next_state)
        delta = next_value - current_value
        
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current = next_state
            current_value = next_value
            
            if current_value > best_value:
                best = current
                best_value = current_value
        
        temperature *= cooling_rate
    
    return best
