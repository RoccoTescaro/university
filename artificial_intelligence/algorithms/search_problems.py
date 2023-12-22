class problem:
    def __init__(self, initial, goal=None):
        self.s_0 = initial
        self.g = goal

    def actions(self, state): 
        # depends heavily on the problem
        pass

    def result(self, state, action):
        # depends heavily on the problem 
        pass

    def is_goal(self, state):
        return state == self.g or state in self.g

class node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.s = state
        self.p = parent
        self.a = action
        self.g = path_cost

class priority_queue:
    def __init__(self, f):
        self.f = f
        self.q = []
    
    def append(self, node):
        self.q.append(node)
        self.q.sort(key=self.f)

    def pop(self):
        return self.q.pop(0)

class fifo_queue:
    def __init__(self):
        self.q = []
    
    def append(self, node):
        self.q.append(node)

    def pop(self):
        return self.q.pop(0)

class lifo_queue:
    def __init__(self):
        self.q = []
    
    def append(self, node):
        self.q.append(node)

    def pop(self):
        return self.q.pop()

def tree_search(problem, frontier, depth = -1):
    frontier.append(node(problem.s_0))
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.s):
            return node
        if depth != -1 and node.g < depth:
            for action in problem.actions(node.s):
                # we are considering the path cost to be 1 for all actions -> child.g = parent.g + 1
                child = node(problem.result(node.s, action), node, action, node.g + 1) 
                frontier.append(child)
    return None

def best_first_search(problem, f):
    frontier = priority_queue(f)
    return tree_search(problem, frontier)

def breadth_first_search(problem):
    frontier = fifo_queue()
    return tree_search(problem, frontier)

def uniform_cost_search(problem):
    return best_first_search(problem, lambda node: node.g)

# should probably check for cycles
def depth_first_search(problem): 
    frontier = lifo_queue()
    return tree_search(problem, frontier)

def depth_limited_search(problem, depth):
    frontier = lifo_queue()
    return tree_search(problem, frontier, depth)

def iterative_deepening_search(problem):
    depth = 0
    while True:
        frontier = lifo_queue()
        result = depth_limited_search(problem, frontier, depth)
        if result != None:
            return result
        depth += 1