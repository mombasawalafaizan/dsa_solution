from collections import deque

def buildTreeUtil(ino, post, inStr, inEnd, pIdx, mapp):
    if inStr > inEnd:
        return None
    cur = post[pIdx[0]]
    pIdx[0]-=1
    nnode = TreeNode(cur)
    if inStr == inEnd:
        return nnode
    inIdx = mapp[cur]
    nnode.right = buildTreeUtil(ino, post, inIdx+1, inEnd, pIdx, mapp)
    nnode.left = buildTreeUtil(ino, post, inStr, inIdx - 1, pIdx, mapp)
    return nnode

def buildtree(inorder, postorder, n):
    # code here
    # build tree and return root TreeNode
    mapp = {x:y for y, x in enumerate(inorder)}
    return buildTreeUtil(inorder, postorder, 0, n-1, [n-1], mapp)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None   

def preorder(node):
    if node:
        print(node, end=' ')
        preorder(node.left)
        preorder(node.right)


if __name__ == "__main__":
    # ino = [26, 29, 34, 36, 38, 43, 46, 74, 80, 81, 96, 100]
    # post = [29, 26, 36, 43, 38, 34, 80, 74, 100, 96, 81, 46]
    ino = [26, 29, 34, 36, 38, 43]
    post = [29, 26, 36, 43, 38, 34]
    root = buildtree(ino, post, len(ino))
    preorder(root)
    print()