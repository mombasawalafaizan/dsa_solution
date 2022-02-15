def isHeap(root):
    #Code Here
    if not root:
        return True
    if root.left or root.right:
        if root.left and root.data < root.left.data:
            return False
        if root.right and root.data < root.right.data:
            return False
    return isHeap(root.left) and isHeap(root.right)