from collections import deque

pos = 0
def buildTreeUtil(ino, pre, inStart, inEnd,mapp):
    global pos
    if inStart > inEnd: 
        return None
    # Pick current node from Preorder traversal using preIndex  
    # and increment preIndex
    cur = pre[pos] 
    nnode = TreeNode(pre[pos])
    pos+=1
    # If no children then return
    if inStart == inEnd:
        return nnode
        
    # Else find the index of this node in Inorder traversal
  
    inIdx = mapp[cur] 

    # Using index in Inorder traversal, construct left and  
    # right subtress 
    nnode.left = buildTreeUtil(ino, pre, inStart, inIdx - 1, mapp) # Recurse for left subtree
    nnode.right = buildTreeUtil(ino, pre, inIdx + 1, inEnd, mapp)
    return nnode

def buildtree(inorder, preorder, n):
    # code here
    # build tree and return root TreeNode
    global pos
    pos = 0
    mapp = {x:y for y, x in enumerate(inorder)}
    return buildTreeUtil(inorder, preorder, 0, n-1, mapp)

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

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node, end=' ')


if __name__ == "__main__":
    bt = BinaryTree()
    bt.create(list(range(5)))
    postorder(buildtree([3, 1, 4, 0, 5, 2], [0, 1, 3, 4, 2, 5], 6))
