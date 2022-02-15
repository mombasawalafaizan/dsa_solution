from collections import defaultdict, deque

def findSubarraySum(arr, n, k):
    # This dictionary will store the indexes where previous sum was encountered
    prevSum = defaultdict(list)
    ans = 0
    currsum = 0
    for i in range(n):
        currsum += arr[i]
        # If currsum = k, this means that starting from the first element upto 
        # this element sum is k
        if currsum==k:
            print(arr[:i+1])
            ans += 1

        # If there currsum - k encountered before, then starting after that
        # element upto current element has the sum k
        if currsum-k in prevSum:
            for start in prevSum[currsum-k]:
                print(arr[start+1:i+1])
                ans += 1
        prevSum[currsum].append(i)
    return ans

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
    
    def preorder(self, node):
        if node:
            print(node,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    # We will traverse the tree in preorder and if we reach a leaf node,
    # print all the sub-paths from root to leaf path with sum k
    def printKSumPaths(self, node, k, arr=[]):
        """ Finds the paths or sub-paths with sum = k """
        if node:
            arr.append(node.data)
            if not node.left and not node.right:
                findSubarraySum(arr, len(arr), k)
            self.printKSumPaths(node.left, k, arr)
            self.printKSumPaths(node.right, k, arr)
            arr.pop()


def printKPath(root, k):
    path = []
    printKPathUtil(root, path, k)

def printVector(v, i):
    for j in range(i, len(v)):
        print(v[j], end=' ')
    print()

def printKPathUtil(root, path, k):
    if not root:
        return
    path.append(root.data)
    printKPathUtil(root.left, path, k)
    printKPathUtil(root.right, path, k)
    f = 0
    # print('Path', path)
    for j in range(len(path)-1, -1, -1):
        f += path[j]
        if f==k:
            printVector(path, j)
    path.pop()

if __name__ == "__main__":
    bt = BinaryTree()
    bt.create([1, 3, -1, 2, 1, 4, 5, None, None, 1, None, 1, 2, None, 6])
    bt.preorder(bt.root)
    print()
    bt.printKSumPaths(bt.root, 5)
    printKPath(bt.root, 5)