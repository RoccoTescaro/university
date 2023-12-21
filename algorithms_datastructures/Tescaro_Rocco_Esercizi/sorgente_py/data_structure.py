import time
import numpy

class node:
    __nextId = 0

    def __init__(self, data):
        self.data = data
        self.id = self.__nextId
        node.__nextId += 1

    def __eq__(self, other):
        return other and self.id == other.id
    
    def __ne__(self, other):
        return not other or self.id != other.id
    
    def __lt__(self, other):
        return other and self.data < other.data
    
    def __le__(self, other):
        return other and self.data <= other.data
    
    def __gt__(self, other):
        return other and self.data > other.data

    def __ge__(self, other):
        return other and self.data >= other.data

    def __str__(self):
            return str(self.data)

class data_structure:
    def __init__(self, head = None):
        self.head = None
        self.size = 0
        if head:
            self.add(head)

    def add(self, node):
        pass

    def __str__(self):
        pass

    def __len__(self):
        return self.size
    
    def os_select(self, i):
        return self._os_select(i)[0]

    def test_os_select(self, i):
        last_time = time.perf_counter_ns()
        #last_time = time.process_time_ns()
        _, explored = self._os_select(i)
        return [explored, time.perf_counter_ns()-last_time]
        #return [explored, time.process_time_ns()-last_time]

    def _os_select(self, i):
        pass

    def os_rank(self, node):
        return self._os_rank(node)[0]

    def test_os_rank(self, node):
        last_time = time.perf_counter_ns()
        #last_time = time.process_time_ns()
        _, explored = self._os_rank(node)
        return [explored, time.perf_counter_ns()-last_time]
        #return [explored, time.process_time_ns()-last_time]

    def _os_rank(self, node):
        pass

