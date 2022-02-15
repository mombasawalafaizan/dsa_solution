def maxSumSubTree(node, max_sum):
    if node:
        curr_sum = maxSumSubTree(node.left) + maxSumSubTree(node.right) + node.data
        max_sum[0] = max(max_sum[0], curr_sum)
        return curr_sum
    else:
        return 0