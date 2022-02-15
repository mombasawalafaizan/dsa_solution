#User function Template for python3
def helper(node, level, truth, max_depth):
    if node:
        if not node.left and not node.right:
            if max_depth[0] == -1: # For first leaf
                max_depth[0] = level
            elif max_depth[0] != level:
                truth[0] = False
                return 
        helper(node.left, level + 1, truth, max_depth)
        helper(node.right, level + 1, truth, max_depth)
    
    
#Your task is to complete this function
#function should return True/False or 1/0
def check(node):
    #Code here
    truth = [True]
    helper(node, 0, truth, [-1])
    return truth[0]

""" This can also be solved iteratively with the help of level order traversal """

"""Or the same solution but with a different return recursive value"""
# # Recursive function which check whether all leaves are at 
# # same level 
# def checkUtil(root, level): 
      
#     # Base Case  
#     if root is None: 
#         return True
      
#     # If a tree node is encountered 
#     if root.left is None and root.right is None: 
          
#         # When a leaf node is found first time 
#         if check.leafLevel == 0 : 
#             check.leafLevel = level # Set first leaf found 
#             return True
  
#         # If this is not first leaf node, compare its level 
#         # with first leaf's level 
#         return level == check.leafLevel  
  
#     # If this is not first leaf node, compare its level 
#     # with first leaf's level 
#     return (checkUtil(root.left, level+1)and
#             checkUtil(root.right, level+1)) 
  
# def check(root): 
#     level = 0
#     check.leafLevel = 0 
#     return (checkUtil(root, level)) 