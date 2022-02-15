from typing import List


class TreeNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def getLargestValue(self, root):
        while root.right:
            root = root.right
        return root.val

    def getSmallestValue(self, root):
        while root.left:
            root = root.left
        return root.val

    def findValidPredecessorAndSuccessor(self, root, x, pred, succ):
        # if not root:
        #     return
        if root.val == x:
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                pred[0] = temp.val
            if root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                succ[0] = temp.val
            return
        if root.val > x:
            succ[0] = root.val
            self.findValidPredecessorAndSuccessor(root.left, x, pred, succ)
        if root.val < x:
            pred[0] = root.val
            self.findValidPredecessorAndSuccessor(root.right, x, pred, succ)

    def isValidBSTOnMerge(self, parent, child):
        smallest = self.getSmallestValue(child)
        largest = self.getLargestValue(child)
        x = child.val
        pred = [None]
        succ = [None]
        print(parent.val, child.val, smallest, largest, pred, succ)
        self.findValidPredecessorAndSuccessor(parent, x, pred, succ)
        return (pred[0] == None or smallest > pred[0]) and (succ[0] == None or largest < succ[0])

    def printPreorder(self, root):
        if root:
            print(root.val, end=' ')
            self.printPreorder(root.left)
            self.printPreorder(root.right)

    def checkForLeaves(self, node, cur_root, parent, dir, trees, roots, n):
        if not node:
            return None
        if not node.left and not node.right:
            ans = None
            if node.val in roots and self.isValidBSTOnMerge(cur_root, trees[roots[node.val]]):
                # Merge 2 BSTs
                if dir == 'L':
                    parent.left = trees[roots[node.val]]
                else:
                    parent.right = trees[roots[node.val]]
                # Remove the other root and swap with last node
                match_idx = roots[node.val]
                roots[trees[n-1].val] = match_idx
                trees[n-1], trees[match_idx] = trees[match_idx], trees[n-1]
                roots.pop(node.val)
                self.printPreorder(cur_root)
                print("   //", node.val, cur_root.val, roots, end=' ')
                for i in trees:
                    print("    //", i.val, end=' ')
                print()
                ans = self.backtrack(trees, roots, n-1)
                if not ans:
                    trees[n-1], trees[match_idx] = trees[match_idx], trees[n-1]
                    if dir == 'L':
                        parent.left = node
                    else:
                        parent.right = node
                    roots[node.val] = match_idx
                    roots[trees[n-1].val] = n-1
                    print('here')
                    self.printPreorder(cur_root)
                    print("   //", node.val, cur_root.val, roots, end=' ')
                    for i in trees:
                        print("    //", i.val, end=' ')
                    print()
            return ans
        left = self.checkForLeaves(
            node.left, cur_root, node, 'L', trees, roots, n)
        right = self.checkForLeaves(
            node.right, cur_root, node, 'R', trees, roots, n)
        return left if left != None else right

    def backtrack(self, trees, roots, n):
        if n == 1:
            return trees[0]
        for i in range(n):
            if trees[i].left or trees[i].right:
                ans = self.checkForLeaves(
                    trees[i], trees[i], None, '', trees, roots, n)
                if ans:
                    return ans
        return None

    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        n = len(trees)
        roots = dict()
        for i in range(n):
            roots[trees[i].val] = i
        res = self.backtrack(trees, roots, n)
        return res


def convertToTree(arr):
    if len(arr) == 1:
        return TreeNode(arr[0])
    elif len(arr) == 2:
        root = TreeNode(arr[0])
        root.left = TreeNode(arr[1])
        return root
    else:
        root = TreeNode(arr[0])
        if arr[1] != None:
            root.left = TreeNode(arr[1])
        root.right = TreeNode(arr[2])
        return root


if __name__ == "__main__":
    s = Solution()
    # input = [[77, 45], [53, None, 58], [65, 12], [76, None, 79], [10, 3], [24, None, 25], [74, 25], [11, None, 76], [13, None, 38], [67, None, 68], [43, 4], [72, None, 76], [17, None, 30], [35, 25], [37, 36], [44, None, 50], [3, None, 80], [62, None, 69], [70, 15], [20, None, 80], [79, None, 80], [9, 4], [28, None, 49], [22, 4], [
    #     69, 65], [15, None, 53], [80, 64], [71, 69], [68, None, 74], [39, None, 68], [31, None, 62], [36, None, 45], [32, None, 55], [14, None, 78], [26, 21], [38, 22], [63, 30], [40, None, 52], [73, None, 74], [49, 10], [75, 29], [54, None, 75], [7, 1], [64, None, 77], [33, 15], [61, 21], [8, 3], [1, None, 17], [60, None, 64], [59, 42]]
    input = [[2, 1], [7, 2, 9], [9, 8]]
    trees = [convertToTree(i) for i in input]
    print('yes', s.canMerge(trees))
