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
    
    
def pre_order(root:Node):
    if root is None:
        return
    print(root, end=', ')
    pre_order(root.left)
    pre_order(root.right)
    
    

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
                        return 
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        return
    
    
    def delete(self, data):
        if self.search(data):
            if self.root is None:
                raise Exception("empty tree")
            parent = current = self.root
            while True:
                if data == current.data: 
                    
                    # if target node is the root
                    if current == self.root:
                        left_subtree = current.left
                        self.root = current.right
                        try:
                            self.root.left = left_subtree
                        except:
                            pass
                        return
                    
                    # if target node is a leaf 
                    elif (current.left is None) and (current.right is None):
                        if child == 'l':
                            parent.left = None
                        else:
                            parent.right = None
                        return
                    
                    # if target node is an internal node
                    else: 
                        if current.right:
                            left_subtree = current.left
                            if child == 'r':
                                parent.right = current.right
                                parent.right.left = left_subtree
                            else:
                                parent.left = current.right
                                parent.right.left = left_subtree
                            return
                        else:
                            if child == 'r':
                                parent.right = current.left
                            else:
                                parent.left = current.left
                            return 
                        
                elif data < current.data:
                    parent = current
                    current = current.left
                    child = 'l'
                else:
                    parent = current
                    current = current.right
                    child = 'r'
        else:
            raise Exception("target not found")       
                   
                    
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
    

tree1 = Tree()
tree1.insert(5)
tree1.insert(1)
tree1.insert(3)
tree1.insert(2)
tree1.insert(4)
tree1.insert(6)
tree1.insert(8)
tree1.insert(7)
tree1.insert(9)
tree1.insert(10)

print(tree1.search(1))
print(tree1.search(2))
print(tree1.search(5))
print(tree1.search(10))
print(tree1.search(7))
print(tree1.search(100))

pre_order(tree1.root)
print()

# delete the root
tree1.delete(5)
pre_order(tree1.root)
print()

# delete a leaf
tree1.delete(2)
pre_order(tree1.root)
print()

# delete an internal node
tree1.delete(8)
pre_order(tree1.root)
print()

# for i in range(1,8):
#     tree1.delete(i)
#     pre_order(tree1.root)

tree1.delete(1)
pre_order(tree1.root)
print()
tree1.delete(3)
pre_order(tree1.root)
print()
tree1.delete(4)
pre_order(tree1.root)
print()
tree1.delete(6)
pre_order(tree1.root)
print()
tree1.delete(9)
pre_order(tree1.root)
print()
print(tree1.root.data)
tree1.delete(10)
pre_order(tree1.root)
print()
