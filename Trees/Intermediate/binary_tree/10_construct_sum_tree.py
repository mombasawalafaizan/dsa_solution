def toSumTree(node) :
    if not node:
        return 0
    old_data = node.data
    node.data = toSumTree(node.left) + toSumTree(node.right)
    return node.data + old_data
    