def bToDLL(root):
    """ Converts binary tree to doubly linked list in inorder fashion """
    def helper(node, new_root, prev):
        if node:
            helper(node.left, new_root, prev)
            if prev[0]!=None:
                prev[0].right = node
            else:
                new_root[0] = node
            node.left = prev[0]
            prev[0] = node
            helper(node.right, new_root, prev)
        
    new_root = [None]
    prev = [None]
    helper(root, new_root, prev)
    return new_root[0]