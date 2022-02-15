class Solution(object):
    def preorder(self, root, good, cur_max):
        if root:
            if root.val >= cur_max:
                good[0] += 1
                cur_max = root.val
            self.preorder(root.left, good, cur_max)
            self.preorder(root.right, good, cur_max)

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good = [0]
        self.preorder(root, good, -10**5)
        return good[0]
