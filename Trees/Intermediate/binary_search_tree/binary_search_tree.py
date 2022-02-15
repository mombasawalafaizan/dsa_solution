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


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if node == None:
            nnode = TreeNode(val)
            if self.root == None:
                self.root = nnode
            return nnode
        elif val < node.data:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        return node
    
    def search(self, val):
        def helper(node, val):
            if node == None or node.data==val:
                return node
            if val < node.data:
                return helper(node.left, val)
            else:   
                return helper(node.right, val)

        return helper(self.root, val)

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # Searching phase
        if root==None:
            return root
        if root.data > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.data < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # Easy cases
        #    ...                                      ...
        #      12                                       12
        #       \                                         \
        #        23 <- node to be deleted   OR             23 <= node to be deleted
        #      /                                             \
        #     21                                              24
        # Append to 12
        # Add link to the grandparent, if <= 1 child is present
        if root.left == None:
            temp = root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp

        # Else both childs are there,
        # then find the inorder successor, and keep track of its parent
        # skip the inorder successor by making links with its parent
        # The node which will be returned will have data of inorder successor
        # append its child to the parent of the node to be deleted
        else:
            succParent = root
            succ = root.right
            while succ.left:
                succParent = succ
                succ = succ.left
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
            root.data = succ.data
            del succ
            return root


    def preorder(self):
        def helper(node):
            if node:
                print(node, end=' ')
                helper(node.left)
                helper(node.right)
        helper(self.root)
        print()

    def inorder(self):
        def helper(node):
            if node:
                helper(node.left)
                print(node, end=' ')
                helper(node.right)
        helper(self.root)
        print()

    def postorder(self):
        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                print(node, end=' ')
        helper(self.root)
        print()
    
    def levelOrder(self, reverse=False):
        q = deque()
        q.append(self.root)
        while q:
            node = q.popleft()
            print(node, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

    def findPredSucc(self, key):
        def helper(node, key):
            nonlocal pre
            nonlocal suc
            if node.data == key:
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    pre = temp.data
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    suc = temp.data
                return

            if node.data > key:
                suc = node.data
                helper(node.left, key)
            else:
                pre = node.data
                helper(node.right, key)
        pre = None
        suc = None
        helper(self.root, key)
        return (pre, suc)

    def printAllRootToLeaf(self, node = float('inf'), path = []):
        if node == float('inf'):
            node = self.root
        if node:
            if not (node.left or node.right):
                for n in path:
                    print(n, end=' ')
                print(node.data)
                return
            path.append(node.data)
            self.printAllRootToLeaf(node.left, path)
            self.printAllRootToLeaf(node.right, path)
            path.pop()
    
    def min(self):
        if not self.root:
            return None
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.data
    
    def max(self):
        if not self.root:
            return None
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.data
    
            
if __name__ == "__main__":
    bt = BST()
    bt.insert(bt.root, 23)
    bt.insert(bt.root, 12)
    bt.insert(bt.root, 28)
    bt.insert(bt.root, 14)
    bt.insert(bt.root, 31)
    bt.insert(bt.root, 7)
    bt.insert(bt.root, 26)
    bt.insert(bt.root, 27)
    bt.insert(bt.root, 25)
    bt.inorder()
    print(bt.search(31))
    print(bt.findPredSucc(31))
    print("All root to leaf paths: ")
    bt.printAllRootToLeaf()
    print('Maximum: ', bt.max())
    print('Minimum: ', bt.min())
    bt.inorder()
    bt.root = bt.deleteNode(bt.root, 23)
    bt.inorder()