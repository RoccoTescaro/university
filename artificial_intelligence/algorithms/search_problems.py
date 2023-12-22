#TODO complete

class problem:
    def __init__(self, initial, goal=None):
        self.s_0 = initial
        self.g = goal

    def actions(self, state): # depends heavily on the problem
        pass

    def result(self, state, action): # depends heavily on the problem
        pass

    def goal_test(self, state):
        return state == self.g

    def best_first_search():
        node = node(self.s_0, None, None, 0)
        frontier = heapq.heapify([node])
        explored = set()
        while frontier:
            node = heapq.heappop(frontier)
            if self.goal_test(node.state):
                return node
            explored.add(node.state)
            for child in node.expand(self):
                if child.state not in explored and child not in frontier:
                    heapq.heappush(frontier, child)
                elif child in frontier and self.f(child) < self.f(frontier[child]):
                    del frontier[child]
                    heapq.heappush(frontier, child)
        return None

class node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.path_cost < node.path_cost

    def __eq__(self, other):
        return isinstance(other, node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        return node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))

    def solution(self):
        return [node.state for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))