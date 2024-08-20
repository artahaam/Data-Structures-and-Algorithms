class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    
    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None
    
    
    def insert(self, data, root=1):
        node = Node(data)
        if root == 1:
            root = self.root
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
                        current = current.right
                        while current.left:
                            current = current.left
                        current.left = left_subtree
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
                        if current.right and not current.left:
                            left_subtree = current.left
                            if child == 'r':
                                parent.right = current.right
                            else:
                                parent.left = current.right
                            parent.right.left = left_subtree
                            return
                        elif current.left and not current.right:
                            if child == 'r':
                                parent.right = current.left
                            else:
                                parent.left = current.left
                            return 
                        else:
                            if child == 'r':
                                parent.right = current.right
                            else:
                                parent.left = current.right
                            left_subtree = current.left
                            current = current.right
                            while current.left:
                                current = current.left
                            current.left = left_subtree
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


    def find_min(self):
        current = self.root
        while current.left:
                current = current.left
        return current.data
    
    
    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    
    def in_order(self, root=1):
        if root == 1:
            root = self.root
        if root is None:
            return
        self.in_order(root.left)
        print(root, end=', ')
        self.in_order(root.right)
        
    
    def pre_order(self, root=1):
        if root == 1:
            root = self.root
        if root == None:
            return
        print(root, end=', ')
        self.pre_order(root.left)
        self.pre_order(root.right)
        
    
    def post_order(self, root=1):
        if root == 1:
            root = self.root
        if root == None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root, end=', ')
        

if __name__ == '__main__':
    # creating a Tree object
    tree = Tree()
    tree.insert(4)
    tree.insert(1)
    tree.insert(3)
    tree.insert(2)
    tree.insert(6)
    tree.insert(7)
    tree.insert(5)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)

    # delete the root node
    tree.delete(4)
    tree.pre_order()
    print()

    # delete an internal node
    tree.delete(5)
    tree.pre_order()
    print()
    
    # delete a leaf node
    tree.delete(2)
    tree.pre_order()
    print()
    
    # tree traversal
    print('*'*11 + ' traversal ' + '*'*11)
    print('pre-order: ')
    tree.pre_order()
    print('\n')
    print('in-order: ')
    tree.in_order()
    print('\n')
    print('post-order: ')
    tree.post_order()
    print()
    print('*'*34, end='\n')

    # search in tree
    print("search in tree")
    print(tree.search(1))
    print(tree.search(0))
    print(tree.search(2))
    print(tree.search(5))
    print(tree.search(10))
    print(tree.search(7))
    print(tree.search(100))
    print('\n') 
    
    # finding the min node
    print(tree.find_min())
    
    # finding the max node
    print(tree.find_max())
    
    
    