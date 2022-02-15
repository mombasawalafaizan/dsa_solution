def LCA(root, n1, n2):
    # Code here
    if root == None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)
    if left and right:
        return root
    return left if left!=None else right


# function to find distance of any node
# from root
def findLevel(root, data, d, level):
     
    # Base case when tree is empty
    if root is None:
        return
 
    # Node is found then append level
    # value to list and return
    if root.data == data:
        d.append(level)
        return
 
    findLevel(root.left, data, d, level + 1)
    findLevel(root.right, data, d, level + 1)


def findDistance(root, n1, n2):
    lca = LCA(root, n1, n2)
    d1 = []
    d2 = []
    if lca:
        findLevel(lca, n1, d1, 0)

        findLevel(lca, n2, d2, 0) 
        return d1[0] + d2[0]
    else:
        return -1