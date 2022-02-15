import math


class Solution(object):
    def recursion(self, preorder, idx, visit, n):
        if idx > n:
            return n
        if preorder[idx] == '#':
            visit[0] += 1
            return idx
        left = self.recursion(preorder, idx + 1, visit, n)
        right = self.recursion(preorder, left + 1, visit, n)
        if left < n and right < n:
            visit[0] += 1
        return right

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        n = len(nodes)
        visit = [0]
        self.recursion(nodes, 0, visit, n)
        return n == visit[0]


s = Solution()
s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
