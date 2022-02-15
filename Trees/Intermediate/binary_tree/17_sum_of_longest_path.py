
def helper(node, level):
    if node:
        left_level_sum = helper(node.left, level+1)
        right_level_sum = helper(node.right, level+1)
        # Check for max_level
        if left_level_sum[0] < right_level_sum[0]:
            right_level_sum[1] += node.data
            return right_level_sum
        elif left_level_sum[0] > right_level_sum[0]:
            left_level_sum[1] += node.data
            return left_level_sum
        # If max_level_sum are same return maximum sum from the two paths
        else:
            return [left_level_sum[0],
            max(left_level_sum[1], right_level_sum[1]) + node.data]
    else:
        return [level-1, 0]
        
def sumOfLongRootToLeafPath(root):
    max_level, max_sum = helper(root, 0)
    return max_sum