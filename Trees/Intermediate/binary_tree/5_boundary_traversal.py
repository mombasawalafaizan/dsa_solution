"""Didn't get accepted by GFG over some stupid nonsense testcase, but I think it's right"""
def printBoundaryView(root):
    # Code here
    def leftView(root, level, store):
        if root:
            if level > len(store)-1:
                store.append(root)
            elif not root.left and not root.right:
                store.append(root)
            leftView(root.left, level+1, store)
            leftView(root.right, level+1, store)
            
    def rightView(root, level, checker, store):
        if root:
            if level > len(store)-1 and checker[level]!=root:
                store.append(root)
            rightView(root.right, level+1, checker, store)
            rightView(root.left, level+1, checker, store)
            
    left = []
    leftView(root, 0, left)
    right = []
    rightView(root, 0, left, right)
    rightmost = left[-1]
    pos = 0
    while pos < len(right) and right[pos]!=rightmost:
        pos += 1
    
    ans = [i.data for i in left]
    ans.extend([j.data for j in right[pos-len(right)-1::-1]])
    return ans


""" Implementation from GFG using Recursion """
ans= []
def printLeft(root):
    global ans
    if root:
        if root.left:
            ans.append(root.data)
            printLeft(root.left)
        elif root.right:
            ans.append(root.data)
            printLeft(root.right)
            
def printRight(root):
    global ans
    if root:
        if root.right:
            printRight(root.right)
            ans.append(root.data)
        elif root.left:
            printRight(root.left)
            ans.append(root.data)
            
def printLeaves(root):
    global ans
    if root:
        printLeaves(root.left)
        if not root.left and not root.right:
            ans.append(root.data)
        printLeaves(root.right)
# your task is to complete this function
# function should return a list containing the boundary view of the binary tree
def printBoundaryViewGFG(root):
    global ans
    if root:
        ans = []
        ans.append(root.data)
        printLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printRight(root.right)
        return ans
    else:
        return []
    
from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.data < other.data

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self, list_of_values):
        """ Create a tree from a given list of value
        eg. [1, 5, 2, None, 4, 7]
        will create a tree like
                        1
                      /    \ 
                    5       2
                     \     /
                      4   7                                  """
        q = deque()
        if not list_of_values or list_of_values[0]==None:
            self.root = None
            return
        self.root = TreeNode(list_of_values[0])
        q.append(self.root)
        idx = 1
        while q:
            cur_node = q.popleft()
            if idx < len(list_of_values):
                if list_of_values[idx]:
                    cur_node.left = TreeNode(list_of_values[idx])
                    q.append(cur_node.left)
                else:
                    cur_node.left = None
                idx += 1
            else:
                break
            if idx < len(list_of_values):
                if list_of_values[idx]:
                    cur_node.right = TreeNode(list_of_values[idx])
                    q.append(cur_node.right)
                else:
                    cur_node.right = None
                idx += 1
            else:
                break

if __name__ == "__main__":
    bt = BinaryTree()
    # For this case, GFG implementation is not correct according to me
    # So, I propose my implementation for this case
    bt.create([4, 10, None, 5, 5, None, 6, 7, None, 8, 8, None, 8, 11, None, 3, 4, None, 1, 3, None, 8, 6, None, 11, 
    11, None,5 ,8])

    print(printBoundaryView(bt.root))
    print(printBoundaryViewGFG(bt.root))
