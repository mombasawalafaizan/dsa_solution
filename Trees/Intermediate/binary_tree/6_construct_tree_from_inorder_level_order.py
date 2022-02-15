class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


"""This solution has O(n^3) time complexity"""

def addNode(node, value, ino):
    found = False
    for i in ino:
        if i == value:
            found = True
        if i == node.data:
            # If found in left, then go to left
            if found: 
                if node.left:
                    addNode(node.left, value, ino)
                else:
                    node.left = Node(value)
            # Else, go to right
            else:
                if node.right:
                    addNode(node.right, value, ino)
                else:
                    node.right = Node(value)
            break
        

def buildTree(level, ino):
    #code here
    #return root of tree
    if not level:
        return None
    root = Node(level[0]) # First node of level order is root
    # For each node of level order, check if the node then occurs left or right
    # If it occurs in left, then check there is already a leftsubtree present or
    # if it is in right subtree if it occurs after that 
    # then recurse until a None is found and add it
    for i in range(1, len(level)): 
        addNode(root, level[i], ino)
    return root