from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def createFromStringBracket(self, s):
        if not s:
            return
        stack = deque()
        node = TreeNode(s[0])
        self.root = node
        stack.append(node)
        i = 1
        while i < len(s):
            if s[i]=='(':
                if stack:
                    node = TreeNode(s[i+1])
                    if stack[-1].left:
                        stack[-1].right = node
                    else:
                        stack[-1].left = node
                    stack.append(node)
                    i += 2
                else:
                    print('Incorrect input')
                    return
            elif s[i]==')':
                stack.pop()
                i += 1


    def inorder(self, node=float('inf')):
        if node == float('inf'):
            node =self.root
        if node:
            self.inorder(node.left)
            print(node, end=' ')
            self.inorder(node.right)

if __name__ == "__main__":
    bt = BinaryTree()
    mystr = 'a(b(c(d)(e(f)(g))))(h(i)(j(k)))'
    bt.createFromStringBracket(mystr)
    bt.inorder()
    print()