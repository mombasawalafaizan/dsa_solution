def kthAncestor(root, node, k):
    if not root:
        return None
    
    if (root.data == node) or (kthAncestor(root.left, node, k)\
        or kthAncestor(root.right, node, k)):
        if k[0] > 0:
            k[0] -= 1    
        elif k[0]==0:
            print('kth ancestor is', root.data)
            return None
        return root