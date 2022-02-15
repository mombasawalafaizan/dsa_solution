# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def calculateSum(self, root):
        if root:
            left = self.calculateSum(root.left)
            right = self.calculateSum(root.right)
            return left + right + root.val
        return 0

    def maximizeProduct(self, root, total, prod):
        if root:
            left = self.maximizeProduct(root.left, total, prod)
            right = self.maximizeProduct(root.right, total, prod)
            cur_sum = left + right + root.val
            prod[0] = max(prod[0], cur_sum * (total-cur_sum))
            return cur_sum
        return 0

    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sumoftree = self.calculateSum(root)
        maxProd = [0]
        self.maximizeProduct(root, sumoftree, maxProd)
        return maxProd[0] % (10**9 + 7)
