def getCountOfNode(root,l,h):
    ##Your code here
    if root:
        left = getCountOfNode(root.left, l, h)
        right = getCountOfNode(root.right, l, h)
        if root.data >= l and root.data <= h:
            return left + right + 1
        else:
            return left + right
    else:
        return 0

# Improved and efficient version
def getCountOfNode(root, l, h):
    if root == None:
        return 0
    
    #Special optional case for improving efficiency
    if root.data == h and root.data == l:
        return 1

    if root.data >= l and root.data <= h:
        return 1 + getCountOfNode(root.left, l, h) + getCountOfNode(root.right, l, h)

    # If current node is smaller than low, then recur for right child 
    elif root.data < l:
        return getCountOfNode(root.right, l, h)
    
    # Else recur for left child 
    else:
        return getCountOfNode(root.left, l, h)

    