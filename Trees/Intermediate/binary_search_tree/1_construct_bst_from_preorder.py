# A Binary tree node 
class Node: 
  
    # Constructor to created a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

# A recursive function to construct BST from pre[]. 
# preIndex is used to keep track of index in pre[] 
def constructTreeUtil(preorder, key, curIdx, mini, maxi, size):
    if curIdx[0] >= size:
        return None
    node = None

    # If current element of pre[] is in range, then  
    # only it is part of current subtree 
    if key > mini and key < maxi:

        # Allocate memory for root of this subtree  
        # and increment constructTreeUtil.preIndex
        node = Node(key)
        curIdx[0] += 1
        if curIdx[0] < size:
            # Construct the subtree under root  
            # All nodes which are in range {min.. key} will 
            # go in left subtree, and first such node will  
            # be root of left subtree 
            node.left = constructTreeUtil(preorder, preorder[curIdx[0]], mini, key, size)

            # All nodes which are in range{key..max} will 
            # go to right subtree, and first such node will 
            # be root of right subtree 
            node.right = constructTreeUtil(preorder, preorder[curIdx[0]], key, maxi, size)
    return node

def constructTree(pre): 
    curIdx = [0]
    size = len(pre) 
    return constructTreeUtil(pre, pre[0], curIdx, float('-inf'), float('inf'), size) 