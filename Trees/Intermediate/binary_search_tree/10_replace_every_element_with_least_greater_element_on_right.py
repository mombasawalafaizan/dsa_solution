class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    root = None
    succ = None
    
    def insert(self, node, val):
        if node == None:
            node = Node(val)
        elif val < node.data:
            BST.succ = node
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        return node

    
def replace(arr, n):
    tree = BST()
    for i in range(n-1, -1, -1):
        BST.succ = None
        BST.root = tree.insert(tree.root, arr[i])
        if BST.succ!=None:
            arr[i] = BST.succ.data
        else:
            arr[i] = -1
        
if __name__ == "__main__":
    arr = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
    replace(arr, len(arr))
    print(arr)