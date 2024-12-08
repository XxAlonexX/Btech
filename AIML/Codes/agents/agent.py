class Environment:
    def __init__(self):
        self.agents = []
        self.state = None
    
    def add_agent(self, agent):
        self.agents.append(agent)
        agent.environment = self
    
    def step(self):
        actions = [agent.get_action(self.state) for agent in self.agents]
        self.state = self.update_state(actions)
        for agent in self.agents:
            agent.perceive(self.state)
    
    def update_state(self, actions):
        raise NotImplementedError
    
    def run(self, steps):
        for _ in range(steps):
            self.step()

class Agent:
    def __init__(self):
        self.environment = None
        self.performance = 0
    
    def get_action(self, state):
        raise NotImplementedError
    
    def perceive(self, state):
        pass

class ReflexAgent(Agent):
    def __init__(self, rules):
        super().__init__()
        self.rules = rules
    
    def get_action(self, state):
        for condition, action in self.rules:
            if condition(state):
                return action

class ModelBasedAgent(Agent):
    def __init__(self, model, planner):
        super().__init__()
        self.model = model
        self.planner = planner
        self.internal_state = None
    
    def get_action(self, state):
        self.internal_state = self.model.update(self.internal_state, state)
        return self.planner.plan(self.internal_state)
    
    def perceive(self, state):
        self.internal_state = self.model.update(self.internal_state, state)

class GoalBasedAgent(Agent):
    def __init__(self, goal, planner):
        super().__init__()
        self.goal = goal
        self.planner = planner
        self.plan = []
    
    def get_action(self, state):
        if not self.plan:
            self.plan = self.planner.plan(state, self.goal)
        return self.plan.pop(0) if self.plan else None
