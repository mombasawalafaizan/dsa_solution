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

    def nthInorder(self, n):
        stack = deque()
        traversed = 0
        cur = self.root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                traversed += 1
                if traversed == n:
                    print(cur, end=' ')
                    break
                cur = cur.right
            else:
                break

    """Recursive function"""
    # count = [0]
    # def NthInorder(node, n): 
  
        # if (node == None): 
        #     return
    
        # if (count[0] <= n): 
    
        #     """ first recur on left child """
        #     NthInorder(node.left, n)  
        #     count[0] += 1
    
        #     # when count = n then prelement  
        #     if (count[0] == n): 
        #         print(node.data, end = " ")  
    
        #     """ now recur on right child """
        #     NthInorder(node.right, n) 


if __name__ == "__main__":
    bt = BinaryTree()
    bt.create([10, 20, 30 , 40, None, 50, 60, 70, None, 80])
    bt.nthInorder(6)