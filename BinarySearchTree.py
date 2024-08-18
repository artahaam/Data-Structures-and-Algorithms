class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    
    def __str__(self):
        return str(self.data)

        
def in_order(root:Node):
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
            while True:
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
                   
                    
    def search(self, data):
        current = self.root
        while True:
            if data == current.data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right

            if current == None:
                return False
    
    
                      

tree = Tree()
tree.insert(5)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(10)
in_order(tree.root)
print()

print(tree.search(1))
print(tree.search(2))
print(tree.search(5))
print(tree.search(10))
print(tree.search(7))
print(tree.search(100))

