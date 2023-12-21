from data_structure import *

class bt_node(node):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None
        self.left = None
        self.right = None

class binary_tree(data_structure):
    def __str__(self):
        itt = self.head
        s = "[ " + ("  " if not itt else "")
        s += self._print("", itt)
        s = s[:-2] + " ]"
        return s
    
    def _print(self, s, node):
        if not node:
            return s
        
        s = self._print(s, node.left)
        s += str(node) + ", "
        s = self._print(s, node.right)
        return s

    def add(self, node):
        assert node
        self.size += 1

        if not self.head:
            self.head = node
            return self

        self._add(self.head, node)
        return self
    
    def _add(self, itt, node):
        node.parent = itt
        if node <= itt:
            if itt.left:
                self._add(itt.left, node)
            else:
                itt.left = node
        else:
            if itt.right:
                self._add(itt.right, node)
            else:
                itt.right = node

    def _os_select(self, i):
        assert self.head and i < self.size and i > 0
        node, _, explored = self.__os_select(self.head, i, 0, -1)
        return node, explored

    def __os_select(self, node, i, index, explored):
        if not node:
            return None, index, explored
        
        left_result, index, explored = self.__os_select(node.left, i, index, explored)
        
        if left_result:
            return left_result, index, explored+1
        
        index += 1
        
        if index == i:
            return node, index, explored+1
        
        return self.__os_select(node.right, i, index, explored+1)
               
    def _os_rank(self, node):
        assert node and self.head
        _, index, explored = self.__os_rank(self.head, node, 0, -1)
        return index, explored
    
    def __os_rank(self, itt, node, index, explored):
        if not itt:
            return None, index, explored
        
        left_result, index, explored = self.__os_rank(itt.left, node, index, explored)
        
        if left_result:
            return left_result, index, explored+1
        
        index += 1
        
        if itt == node:
            return itt, index, explored+1
        
        return self.__os_rank(itt.right, node, index, explored+1)
