def populateNextRecur(root, next):
    if root:
        populateNextRecur(root.right, next)
        root.next = next[0]
        next[0] = root
        populateNextRecur(root.left, next)
    
def populateNext(root):
    next = [None]
    populateNextRecur(root, next)