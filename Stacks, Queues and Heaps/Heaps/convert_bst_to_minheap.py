class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.data)
        inorder(root.right, arr)

def convertUsingPreorder(root, ino, i):
    if root:
        root.data = ino[i[0]]
        i[0] += 1
        convertUsingPreorder(root.left, ino, i)
        convertUsingPreorder(root.right, ino, i)


def convertToMinHeapUtil(root):
    ino = []
    inorder(root, ino)
    i = [0]
    convertUsingPreorder(root, ino, i)
    

def preorderTraversal(root):
    if root:
        print(root.data , end=' ')
        preorderTraversal(root.left)
        preorderTraversal(root.right)

if __name__ == '__main__': 
      
    # BST formation  
    root = Node(4) 
    root.left = Node(2)  
    root.right = Node(6)  
    root.left.left = Node(1) 
    root.left.right = Node(3)  
    root.right.left = Node(5)  
    root.right.right = Node(7)  
  
    convertToMinHeapUtil(root) 
    print("Preorder Traversal:")  
    preorderTraversal(root)  
    print()