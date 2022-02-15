def inOrder(root, ino):
    if root:
        inOrder(root.left, ino)
        ino.append(root.data)
        inOrder(root.right, ino)

def modify(root, required, pos):
    if root:
        modify(root.left, required, pos)
        root.data = required[pos[0]]
        pos[0] += 1
        modify(root.right, required, pos)
        
# The given root is the root of the Binary Tree
# Return the root of the generated BST
def binaryTreeToBST(root):
    # code here
    previous_ino = []
    inOrder(root, previous_ino)
    required_ino = sorted(previous_ino)
    modify(root, required_ino, [0])
    return root