class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.data
    

def in_order(root:TreeNode):
    if root is None:
        return
    in_order(root.left)
    print(root, end=', ')
    in_order(root.right)
    
    
def pre_order(root:TreeNode):
    if root is None:
        return
    print(root, end=', ')
    pre_order(root.left)
    pre_order(root.right)
    
    
def post_order(root:TreeNode):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root, end=', ')
    

if __name__ == '__main__':
        
    n0 = TreeNode('0')
    n1 = TreeNode('1')
    n2 = TreeNode('2')
    n3 = TreeNode('3')
    n4 = TreeNode('4')
    n5 = TreeNode('5')

    n0.left = n1
    n0.right = n2
    n1.left = n3
    n3.left = n4
    n3.right = n5


    in_order(n0)
    print()
    pre_order(n0)
    print()
    post_order(n0)