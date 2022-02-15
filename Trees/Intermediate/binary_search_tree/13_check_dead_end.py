def getInorder(root, ino, leaves):
    if root:
        getInorder(root.left, ino, leaves)
        ino.append(root.data)
        if not root.left and not root.right:
            leaves.append(root.data)
        getInorder(root.right, ino, leaves)

# Check if the inorder predecessor and successor of leaf 
# allows it to enter a node with distinct value
def isdeadEnd(root):
    """Function returns true if the bst contains a dead end, else false"""
    # You can also use a set(hashmap) for fast calculations
    ino = []
    leaves = []
    getInorder(root, ino, leaves)
    j = 0
    for i in range(len(ino)-1):
        if leaves[j] == ino[i]:
            if i==0 and (ino[i]==1 and ino[i+1]==2):
                return True
            if ino[i] == ino[i-1]+1 and ino[i]+1 == ino[i+1]:
                return True
            j += 1
            if j==len(leaves):
                break
    return False