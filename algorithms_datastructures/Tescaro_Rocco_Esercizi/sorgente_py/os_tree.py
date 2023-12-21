from data_structure import *

class os_node(node):
    def __init__(self, data, color = True): #color = False for black, True for red
        super().__init__(data)
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1
        self.color = color 

class os_tree(data_structure):
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
            node.color = False
            return self

        parent = None
        itt = self.head
        while itt:
            parent = itt
            parent.size += 1
            if node <= itt:
                itt = itt.left
            else:
                itt = itt.right
        
        node.parent = parent
        if node <= parent:
            parent.left = node
        else:
            parent.right = node

        self._fixup(node)
        return self

    def _fixup(self, node):
        while node.parent and node.parent.color:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self._left_rotate(node.parent.parent)
        self.head.color = False

    def _left_rotate(self, node):
        assert node and node.right
        right = node.right
        node.right = right.left
        if right.left:
            right.left.parent = node
        right.parent = node.parent
        if not node.parent:
            self.head = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right
        right.size = node.size
        node.size = 1
        if node.left:
            node.size += node.left.size
        if node.right:
            node.size += node.right.size
    
    def _right_rotate(self, node):
        assert node and node.left
        left = node.left
        node.left = left.right
        if left.right:
            left.right.parent = node
        left.parent = node.parent
        if not node.parent:
            self.head = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left
        left.size = node.size
        node.size = 1
        if node.left:
            node.size += node.left.size
        if node.right:
            node.size += node.right.size

    def _os_select(self, i):
        assert self.head and i < self.size and i > 0
        return self.__os_select(self.head, i)
    
    def __os_select(self, node, i):
        if not node:
            return None, 0
    
        l_size = 0
        if node.left:
            l_size = node.left.size 

        if i == l_size + 1:
            return node, 1
        elif i <= l_size:
            a, b = self.__os_select(node.left, i)
            return a, b + 1
        else:
            a, b = self.__os_select(node.right, i - l_size - 1)
            return a, b + 1

    def _os_rank(self, node):
        assert node and self.head
        return self.__os_rank(self.head, node)

    def __os_rank(self, itt, node):
        if not itt:
            return 0, 0

        l_size = 0
        if itt.left:
            l_size = itt.left.size
        if itt == node:
            return l_size + 1, 1
        elif node < itt:
            return self.__os_rank(itt.left, node)
        else:
            a, b = self.__os_rank(itt.right, node)
            return l_size + 1 + a, b + 1