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


    def insert(self, val):
        """ Given a binary tree and a key, insert the key into the binary tree 
        at first position available in level order. """
        nnode = TreeNode(val)
        if not self.root:
            self.root = nnode
            return
        q = deque()
        q.append(self.root)
        while q:
            cur = q.popleft()
            if not cur.left:
                cur.left = nnode
                break
            else:
                q.append(cur.left)
            if not cur.right:
                cur.right = nnode
                break
            else:
                q.append(cur.right)
    
    def delete(self, key):
        root = self.root
        if not root:
            self.root = None
        if root.left==None and root.right==None:
            if root.data == key:
                self.root =  None
            else:
                self.root =  root
        q = deque()
        q.append(self.root)
        key_node = None
        temp = None
        while q:
            temp = q.popleft()
            if temp.data == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x = temp.data # Deepest Rightmost node is temp
            self.__deleteDeepest(temp)
            key_node.data = x
        self.root =  root

    # function to delete the given deepest node (d_node) in binary tree  
    def __deleteDeepest(self, d_node): 
        q = deque()
        q.append(self.root) 
        while(len(q)): 
            temp = q.popleft() 
            if temp is d_node: 
                temp = None
                return
            if temp.right: 
                if temp.right is d_node: 
                    temp.right = None
                    return
                else: 
                    q.append(temp.right) 
            if temp.left: 
                if temp.left is d_node: 
                    temp.left = None
                    return
                else: 
                    q.append(temp.left) 

    """Traversals"""
    def inorder(self, node=None, recursive = True):
        if recursive:
            if node:
                BinaryTree.__inorder(node)
            else:
                BinaryTree.__inorder(self.root)
        else:
            if node:
                BinaryTree.__inorderIterative(node)
            else:
                BinaryTree.__inorderIterative(self.root)

    @staticmethod
    def __inorder(node):
        if node!=None:
            BinaryTree.__inorder(node.left)
            print(node, end=' ')
            BinaryTree.__inorder(node.right)
    
    @staticmethod
    def __inorderIterative(node):
        if not node:
            return
        stack = deque()
        stack.append(node)
        temp = node
        while stack:
            temp = stack.pop()

            while temp.left:
                stack.append(temp)
                temp = temp.left

            while stack and temp.right==None:
                print(temp, end=' ')
                temp = stack.pop()
            print(temp, end=' ')
            if temp.right:
                stack.append(temp.right)

        ## GFG implementation
        # stack = deque()
        # current = node
        # while True:
        #     if current:
        #         stack.append(current)
        #         current = current.left
        #     elif stack:
        #         current = stack.pop()
        #         print(current, end= ' ')
        #         current = current.right
        #     else:
        #         break
        print()

    def preorder(self, node=None, recursive = True):
        if recursive:
            if node:
                BinaryTree.__preorder(node)
            else:
                BinaryTree.__preorder(self.root)
        else:
            if node:
                BinaryTree.__preorderIterative(node)
            else:
                BinaryTree.__preorderIterative(self.root)

    @staticmethod
    def __preorder(node):
        if node!=None:
            print(node, end=' ')
            BinaryTree.__preorder(node.left)
            BinaryTree.__preorder(node.right)

    @staticmethod
    def __preorderIterative(node):
        if not node:
            return
        stack = deque()
        stack.append(node)
        while stack:
            temp = stack.pop()
            while temp:
                print(temp, end=' ')
                if temp.right:
                    stack.append(temp.right)
                temp = temp.left  

    
    def postorder(self, node=None, recursive = True):
        if recursive:
            if node:
                BinaryTree.__postorder(node)
            else:
                BinaryTree.__postorder(self.root)
        else:
            if node:
                BinaryTree.__postorderIterative(node)
            else:
                BinaryTree.__postorderIterative(self.root)

    @staticmethod
    def __postorder(node):
        if node!=None:
            BinaryTree.__postorder(node.left)
            BinaryTree.__postorder(node.right)
            print(node, end=' ')
    
    @staticmethod
    def __postorderIterative(node):
        if not node:
            return
        stack = deque()
        while True:
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                if stack and node.right == stack[-1]:
                    stack.pop()
                    stack.append(node)
                    node = node.right
                else:
                    print(node, end=' ')
                    node = None
            else:
                break
        print()

    def search(self, node=float('inf'), key=float('inf')):
        if node == float('inf'):
            node = self.root
        if node:
            if node.data == key:
                return True
            return self.search(node.left, key) or self.search(node.right, key)
        return False

    def levelOrder(self, reverse=False):
        q = deque()
        q.append(self.root)
        stack = deque()
        while q:
            node = q.popleft()
            if reverse:
                stack.append(node)
            else:
                print(node, end=' ')
            if not reverse:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        if reverse:
            while stack:
                print(stack.pop(), end=' ')
        print()

    def height(self, node = float('inf')):
        if node == float('inf'):
            node = self.root
        if not node:
            return -1
        else:
            return max(self.height(node.left)+1, self.height(node.right)+1) 

    def isBalanced(self, node = float('inf')):
        def helper(node, balanced):
            if not node:
                return 0
            else:
                left_height = helper(node.left, balanced)
                right_height = helper(node.right, balanced)
                balanced[0] = balanced[0] and (abs(left_height - right_height) <= 1)
                return max(left_height, right_height) + 1
        balanced = [True]
        helper(self.root, balanced)
        return balanced[0]

    def isBST(self, node = float('inf'), mini = None, maxi = None):
        """ This method checks whether left subtree is less then the root 
            and right subtree is greater than the root 
            mini: For right subtree every node must be greater than minimum value
            maxi: For left subtree every node must be lesser than maximum value"""
        if node == float('inf'):
            node = self.root
        if node:
            if mini!=None and node.data <= mini.data:
                return False
            if maxi!=None and node.data >= maxi.data:
                return False
            return self.isBST(node.left, mini, node) and self.isBST(node.right, node, maxi)
        else:
            return True
    
    def isBST_method2(self):
        """Using inorder traversal, keep track of the previous node and check 
        if it is lesser than each node"""
        def helper(node, prev):
            if node:
                if helper(node.left, prev) == False:
                    # prev[0] = node.data
                    return False
                if prev[0] > node.data:
                    return False
                prev[0] = node.data
                return helper(node.right, prev)
            else:
                return True
        prev = [float('-inf')]
        return helper(bt.root, prev)
        
            

    def diameter(self):
        def helper(node, max_so_far):
            if node:
                left_max = helper(node.left, max_so_far) # Height of left subtree
                right_max = helper(node.right, max_so_far) # Height of right subtree
                max_so_far[0] = max(max_so_far[0], left_max+right_max+1) # Maximum diameter so far
                return max(left_max, right_max) + 1
            else:
                return 0
        max_container = [0]
        helper(self.root, max_container)
        return max_container[0]

    def convertToMirror(self, node = float('inf')):
        if node==float('inf'):
            node = self.root
        if node:
            temp = node.left
            node.left = node.right
            node.right = temp
            self.convertToMirror(node.left)
            self.convertToMirror(node.right)

    def min(self, node = float('inf'), min_val = float('inf')):
        if node == float('inf'):
            node = self.root
        if node!=None:
            if min_val > node.data:
                min_val = node.data
            return min(self.min(node.left, min_val), self.min(node.right, min_val))
        else:
            return min_val
        
    def max(self, node = float('inf'), max_val = float('-inf')):
        if node == float('inf'):
            node = self.root
        if node!=None:
            if max_val< node.data:
                max_val = node.data
            return max(self.max(node.left, max_val), self.max(node.right, max_val))
        else:
            return max_val

    def leftView(self, node):
        if node:
            if node.left:
                print(node, end=' ')
                self.leftView(node.left)
            

if __name__ == "__main__":
    bt = BinaryTree()
    # root = TreeNode(2)  
    # root.left     = TreeNode(7)  
    # root.right     = TreeNode(5)  
    # root.left.right = TreeNode(6)  
    # root.left.right.left=TreeNode(1)  
    # root.left.right.right=TreeNode(11)  
    # root.right.right=TreeNode(9)  
    # root.right.right.left=TreeNode(4)  
    root = TreeNode(88) 
    root.left = TreeNode(72) 
    root.left.right = TreeNode(74) 
    root.right = TreeNode(99) 
    root.right.right = TreeNode(100)
    bt.root = root
    # bt.create([23, 12, 28, None, 14, None, 31])
    print("Inorder traversal using recursion:", end = " ") 
    bt.inorder() 
    print() 
    print("Level order traversal: ", end='')
    bt.levelOrder()
    print("Balanced: ", bt.isBalanced())
    print("Height: ", bt.height())
    print('Diameter: ', bt.diameter())
    print('Minimum: ', bt.min())
    print('Maximum: ', bt.max())
    print('Is BST by inorder method?', bt.isBST())
    print('Is BST by mini maxi?', bt.isBST_method2())