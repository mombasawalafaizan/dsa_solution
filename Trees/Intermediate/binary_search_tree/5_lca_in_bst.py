def LCAUtil(root, n1, n2):
    if not root:
        return None
    # If current data is in range [n1, n2], it is
    # the lowest common ancestor of n1 and n2
    if root.data >= n1 and root.data <= n2:
        return root
    if root.data < n1:
        result = LCAUtil(root.right, n1, n2)
    else:
        result = LCAUtil(root.left, n1, n2)
    return result

# Returns the LCA of the nodes with values n1 and n2
# in the BST rooted at 'root' 
def LCA(root, n1, n2):
    # This will ensure that the first argument is less then the second argument
    return LCAUtil(root, min(n1, n2), max(n1, n2))