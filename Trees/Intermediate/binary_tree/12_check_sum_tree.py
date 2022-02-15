def helper(node, truth):
    if node == None:
        return 0
    if not node.left and not node.right: # If leaf node, return value of node
        return node.data
    sum_data = helper(node.left, truth) + helper(node.right, truth)
    # Check if node data is equal to sum of left and right subtree
    if node.data != sum_data:
        truth[0] = False
    return sum_data + node.data
    
# your task is to complete this function
# function should return True is Tree is SumTree else return False
def isSumTree(root):
    # Code here
    truth = [True]
    helper(root, truth)
    return truth[0]