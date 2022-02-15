# METHOD 1
# We can solve this problem by considering the fact that both node and its children can’t be in sum at same time, 
# so when we take a node into our sum we will call recursively for its grandchildren or when we don’t take this node 
# we will call for all its children nodes and finally we will choose maximum from both of these results.
# It can be seen easily that above approach can lead to solving same subproblem many times, for example in above 
# diagram node 1 calls node 4 and 5 when its value is chosen and node 3 also calls them when its value is not chosen 
# so these nodes are processed more than once. We can stop solving these nodes more than once by memoizing the result at all nodes.
# In below code a map is used for memoizing the result which stores result of complete subtree rooted at a node in the map,
#  so that if it is called again, the value is not calculated again instead stored value from map is returned directly.
def sumOfGrandChildren(node, mp):
    sum = 0
    if node.left:
        sum += getMaxSumUtil(node.left.left, mp) + getMaxSumUtil(node.left.right, mp)
    if node.right:
        sum += getMaxSumUtil(node.right.left, mp) + getMaxSumUtil(node.right.right, mp)
    return sum

def getMaxSumUtil(node, mp):
    if not node:
        return 0
    if node in mp:
        return mp[node]
    include = node.data + sumOfGrandChildren(node, mp)
    exclude = sumOfGrandChildren(node.left, mp) + sumOfGrandChildren(node.right, mp)
    mp[node] = max(include, exclude)
    return mp[node]

def getMaxSum(node):
    if not node:
        return 0
    mp = {}
    return getMaxSumUtil(node, mp)




# METHOD 2:
# Return a pair for each node in the binary tree such that first of the pair indicates 
# maximum sum when the data of node is included and second indicates maximum sum when 
# the data of a particular node is not included.

def maxSumHelper(root) : 
  
    if (root == None):  
      
        sum = [0, 0]  
        return sum
      
    sum1 = maxSumHelper(root.left)  
    sum2 = maxSumHelper(root.right)  
    sum = [0, 0] 
  
    # This node is included (Left and right  
    # children are not included)  
    sum[0] = sum1[1] + sum2[1] + root.data  
  
    # This node is excluded (Either left or  
    # right child is included)  
    sum[1] = (max(sum1[0], sum1[1]) + 
              max(sum2[0], sum2[1]))  
  
    return sum

def maxSum(root):
    res = maxSumHelper(root)
    return max(res[0], res[1])