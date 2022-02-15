def storeInorder(root, ino):
    if root:
        storeInorder(root.left, ino)
        ino.append(root)
        storeInorder(root.right, ino)

def createBalanced(ino, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    node = ino[mid]
    node.left = createBalanced(ino, start, mid-1)
    node.right = createBalanced(ino, mid+1, end)
    return node

def makeBalanced(root):
    ino = []
    storeInorder(root, ino)
    n = len(ino)
    return createBalanced(ino, 0, n-1)