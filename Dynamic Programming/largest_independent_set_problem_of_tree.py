# Given a Binary Tree, find size of the Largest Independent Set(LIS) in it. A subset of all tree 
# nodes is an independent set if there is no edge between any two nodes of the subset.

# Python3 program for calculating LISS 
# using dynamic programming 
  
# A binary tree node has data, 
# pointer to left child and a 
# pointer to right child 
class node: 
    def __init__(self, data): 
          
        self.data = data 
        self.left = self.right = None
        self.liss = 0
  
# A memoization function returns size 
# of the largest independent set in 
# a given binary tree 
def liss(root): 
      
    if root == None: 
        return 0
      
    if root.liss != 0: 
        return root.liss 
      
    if (root.left == None and 
        root.right == None): 
        root.liss = 1
        return root.liss 
  
    # Calculate size excluding the 
    # current node 
    liss_excl = (liss(root.left) + 
                 liss(root.right)) 
  
    # Calculate size including the 
    # current node 
    liss_incl = 1
    if root.left != None: 
        liss_incl += (liss(root.left.left) + 
                      liss(root.left.right)) 
          
    if root.right != None: 
        liss_incl += (liss(root.right.left) +
                      liss(root.right.right)) 
          
    # Maximum of two sizes is LISS, 
    # store it for future uses. 
    root.liss = max(liss_excl, liss_incl) 
      
    return root.liss 
      
def lissFaizan(root):
    if not root:
        return [0, 0]
    if not root.left and not root.right: 
        return [1, 0]
    temp = [0, 0] # [include, exclude]
    left = lissFaizan(root.left)
    right = lissFaizan(root.right)
    # If including current node, add the value of children which are not included 
    # i.e cur_node + max_val of grandchildrens
    temp[0] = 1 + left[1] + right[1] 
    # If excluding current node, get the max value from both left and right
    # subtree and add them
    temp[1] = max(left) + max(right)
    return temp

# Driver Code 
  
# Let us construct the tree given 
# in the above diagram 
root = node(20) 
root.left = node(8) 
root.left.left = node(4) 
root.left.right = node(12) 
root.left.right.left = node(10) 
root.left.right.right = node(14) 
root.right = node(22) 
root.right.right = node(25) 
  


print("Size of the Largest Independent Set is ", max(lissFaizan(root))) 