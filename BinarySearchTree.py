class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    
    def __str__(self):
        return str(self.data)

        
def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root, end=', ')
    in_order(root.right)
    

class Tree:
    def __init__(self):
        self.root = None
    
    
    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        break
    

tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(6)
tree.insert(7)
tree.insert(3)
tree.insert(10)
tree.insert(5)
in_order(tree.root)


