def isIsomorphic(root1, root2): 
    #code here.
    if root1==None and root2==None:
        return True
    if root1==None or root2==None:
        return False
    if root1.data == root2.data:
        return (isIsomorphic(root1.left, root2.right) and\
            isIsomorphic(root1.right, root2.left)) or\
            (isIsomorphic(root1.left, root2.left) and\
            isIsomorphic(root1.right, root2.right))
    else:
        return False