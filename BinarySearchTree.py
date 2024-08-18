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

    print('*'*11 + ' traversal ' + '*'*11)
    print('pre-order: ')
    tree1.pre_order()
    print('\n')
    print('in-order: ')
    tree1.in_order()
    print('\n')
    print('post-order: ')
    tree1.post_order()
    print()
    print('*'*34, end='\n')

    print("search wether tree contains specific data")
    print(tree1.search(1))
    print(tree1.search(2))
    print(tree1.search(5))
    print(tree1.search(10))
    print(tree1.search(7))
    print(tree1.search(100))
    print('\n') 
    
    # delete the root
    tree1.delete(5)
    tree1.pre_order()
    print()

    # delete a leaf
    tree1.delete(2)
    tree1.pre_order()
    print()

    # delete an internal node
    tree1.delete(8)
    tree1.pre_order()
    print()


    tree1.delete(1)
    tree1.pre_order()
    print()
    tree1.delete(3)
    tree1.pre_order()
    print()
    tree1.delete(4)
    tree1.pre_order()
    print()
    tree1.delete(6)
    tree1.pre_order()
    print()
    tree1.delete(9)
    tree1.pre_order()
    print()
    print(tree1.root.data)
    tree1.delete(10)
    tree1.pre_order()
    print()
