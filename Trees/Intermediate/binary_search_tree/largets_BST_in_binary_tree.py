class subTreeInfo:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')
        self.nodes = 0
        self.isBST = True
        
def postorder(node, maxlength):
    if node:
        left = postorder(node.left, maxlength)
        right = postorder(node.right, maxlength)
        if left.isBST and right.isBST and \
            node.data > left.max_val and node.data < right.min_val:
            maxlength[0] = max(maxlength[0], left.nodes + right.nodes + 1)
            left.nodes = left.nodes + right.nodes + 1
            left.min_val = min(node.data, left.min_val)
            left.max_val = max(node.data, right.max_val)
            return left
        else:
            left.isBST = False
            return left
    else:
        return subTreeInfo()

# Return the size of the largest sub-tree which is also a BST
def largestBst(root):
    if not root:
        return 0
    maxlength = [1]
    postorder(root, maxlength)
    return maxlength[0]