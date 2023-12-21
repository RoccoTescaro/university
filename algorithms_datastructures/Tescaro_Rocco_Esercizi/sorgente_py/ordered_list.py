from data_structure import *

class ol_node(node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None
        self.prev = None

class ordered_list(data_structure):

    def __str__(self):
        itt = self.head
        s = "[ " + ("  " if not itt else "")
        while itt:
            s += str(itt) + ", "
            itt = itt.next
        s = s[:-2] + " ]"
        return s
    
    def add(self, node): #TODO fix head
        assert node
        self.size += 1

        if not self.head:
            self.head = node
            return self
        elif self.head > node:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return self
        
        itt = self.head
        while itt.next and itt.next < node:
            itt = itt.next

        node.prev = itt

        if not itt.next:
            itt.next = node
            return self
        
        node.next = itt.next
        itt.next.prev = node
        itt.next = node
        return self
    
    def _os_select(self, i):
        assert self.head and i < self.size and i > 0
        
        itt = self.head
        explored = 1
        while itt and explored < i:
            explored += 1
            itt = itt.next
        
        return itt, explored
    

    def _os_rank(self, node):
        assert node and self.head

        itt = self.head
        explored = 1
        while itt and itt != node:
            explored += 1
            itt = itt.next
        
        return explored, explored