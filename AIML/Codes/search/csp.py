class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_complete(self):
        return len(self.assignment) == len(self.variables)

    def is_consistent(self, var, value):
        self.assignment[var] = value
        consistent = all(constraint(self.assignment) 
                        for constraint in self.constraints 
                        if var in constraint.__code__.co_varnames)
        del self.assignment[var]
        return consistent

    def backtrack_search(self):
        if self.is_complete():
            return self.assignment
        
        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value):
                self.assignment[var] = value
                result = self.backtrack_search()
                if result:
                    return result
                del self.assignment[var]
        return None

    def select_unassigned_variable(self):
        unassigned = [v for v in self.variables if v not in self.assignment]
        return min(unassigned, key=lambda var: len(self.domains[var]))

    def order_domain_values(self, var):
        return self.domains[var]

def solve_csp(variables, domains, constraints):
    csp = CSP(variables, domains, constraints)
    return csp.backtrack_search()

def map_coloring_constraint(colors, neighbors):
    def constraint(assignment):
        return all(assignment.get(n1) != assignment.get(n2)
                  for n1, n2 in neighbors
                  if n1 in assignment and n2 in assignment)
    return constraint
