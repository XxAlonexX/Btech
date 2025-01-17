def minimax(state, depth, is_maximizing, get_moves, evaluate):
    if depth == 0 or not get_moves(state):
        return evaluate(state)
        
    if is_maximizing:
        value = float('-inf')
        for move in get_moves(state):
            value = max(value, minimax(move, depth - 1, False, get_moves, evaluate))
        return value
    else:
        value = float('inf')
        for move in get_moves(state):
            value = min(value, minimax(move, depth - 1, True, get_moves, evaluate))
        return value

def alpha_beta(state, depth, alpha, beta, is_maximizing, get_moves, evaluate):
    if depth == 0 or not get_moves(state):
        return evaluate(state)
        
    if is_maximizing:
        value = float('-inf')
        for move in get_moves(state):
            value = max(value, alpha_beta(move, depth - 1, alpha, beta, False, 
                                        get_moves, evaluate))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for move in get_moves(state):
            value = min(value, alpha_beta(move, depth - 1, alpha, beta, True, 
                                        get_moves, evaluate))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def get_best_move(state, depth, get_moves, evaluate, use_alpha_beta=True):
    best_value = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    
    for move in get_moves(state):
        if use_alpha_beta:
            value = alpha_beta(move, depth - 1, alpha, beta, False, get_moves, evaluate)
        else:
            value = minimax(move, depth - 1, False, get_moves, evaluate)
            
        if value > best_value:
            best_value = value
            best_move = move
            
    return best_move
