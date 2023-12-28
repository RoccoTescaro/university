class problem:
    def __init__(self, s_0):
        self.s_0 = s_0
    
    def actions(self, s):
        pass
    
    def result(self, s, a):
        pass
    
    def f(self, s):
        pass

def hill_climbing(problem):
    current = problem.s_0[0]
    while True:
        neighbors = [problem.result(current, action) for action in problem.actions(current)]
        if not neighbors:
            return current
        neighbor = max(neighbors, key = lambda n: problem.f(n))
        if f(neighbor) <= problem.f(current):
            return current
        current = neighbor

def random_restart_hill_climbing(problem, max_sideway = 1000):
    current = problem.s_0
    itt = 0
    while itt < max_sideway:
        neighbors = [problem.result(current, action) for action in problem.actions(current)]
        if not neighbors:
            return current
        neighbor = max(neighbors, key = lambda n: problem.f(n))
        if f(neighbor) <= problem.f(current):
            return current
        current = neighbor
        itt += 1 #should increment itterator only with sideway moves
    return random_restart_hill_climbing(problem, max_sideway)

def stochastic_hill_climbing(problem):
    current = problem.s_0
    while True:
        neighbors = [problem.result(current, action) for action in problem.actions(current)]
        if not neighbors:
            return current
        neighbor = random.choice(neighbors)
        if f(neighbor) <= problem.f(current):
            return current
        current = neighbor

def local_beam_search(problem, k, max_sideway = 1000):
    current = problem.s_0
    itt = 0
    while itt < max_sideway:
        neighbors = [problem.result(s, action) for s in current for action in problem.actions(s.s)]
        if not neighbors:
            return current
        current = sorted(neighbors, key = lambda n: problem.f(n))[-k:]
        itt += 1 #should increment itterator only with sideway moves

'''
def parallel_local_beam_search(problem, k, max_sideway = 1000):
    pass    
'''

def simulated_annealing(problem, schedule):
    current = problem.s_0
    t = 0
    while True:
        T = schedule(t)
        if T == 0:
            return current
        next = random.choice(problem.actions(current))
        delta_e = problem.f(next) - problem.f(current)
        if delta_e > 0 or random.uniform(0, 1) < math.exp(delta_e / T):
            current = next
        t += 1