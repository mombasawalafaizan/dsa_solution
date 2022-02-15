def search(root2, key):
    if root2==None:
        return False
    if root2.data < key:
        return search(root2.right, key)
    elif root2.data > key:
        return search(root2.left, key)
    else:
        return True
        
def inOrderOfTree1(node, root2, x):
    if node:
        inOrderOfTree1(node.left, root2, x)
        inOrderOfTree1(node.right, root2, x)
        if search(root2, x-node.data):
            countPairs.count += 1

def countPairs(root1, root2, x):
    countPairs.count = 0
    inOrderOfTree1(root1, root2, x)
    return countPairs.count

# Method 2;
# Traverse BST 1 from smallest value to node to largest. This can be achieved with the help of iterative inorder traversal.
# Traverse BST 2 from largest value node to smallest. This can be achieved with the help of reverse inorder traversal. Perform these 
# two traversals simultaneously. Sum up the corresponding node’s value from both the BSTs at a particular instance of traversals. 
# If sum == x, then increment count. If x > sum, then move to the inorder successor of the current node of BST 1, else move to the 
# inorder predecessor of the current node of BST 2. Perform these operations until either of the two traversals gets completed.