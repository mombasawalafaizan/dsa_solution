class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None

def insert(node, val):
    if node == None:
        nnode = TreeNode(val)
        return nnode
    elif val < node.data:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node
    
def flatten(node, next):
    if node:
        flatten(node.right, next)
        node.right = next[0]
        if next[0]:
            next[0].left = None
        next[0] = node
        flatten(node.left, next)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

if __name__ == "__main__":
    root = None
    root = insert(root, 25)
    root = insert(root, 23)
    root = insert(root, 27)
    root = insert(root, 22)
    root = insert(root, 24)
    root = insert(root, 26)
    root = insert(root, 28)
    root = insert(root, 93)
    root = insert(root, 14)
    root = insert(root, 1)
    root = insert(root, 9)
    root = insert(root, 94)
    root = insert(root, 62)

    inorder(root)
    print()
    next=[None]
    flatten(root, next)
    root = next[0]
    temp = root
    while temp:
        print(temp.data, end=' ')  
        temp = temp.right