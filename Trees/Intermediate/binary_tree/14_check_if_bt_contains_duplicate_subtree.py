from collections import defaultdict

    
def compare_height_2_sub(node1, node2):
    """ Function to check if two trees are equal """
    
    flag = True
    if node1.left or node2.left:
        if node1.left and node2.left:
            flag = (node1.left.data == node2.left.data)
        else:
            return False
    if node1.right or node2.right:
        if node1.left and node2.left:
            flag = flag and (node1.right.data == node2.right.data)
        else:
            return False
    return flag

def isLeaf(node):
    return node==None or (node.left==None and node.right==None)       

def postorder(node, second_last_level_nodes, truth):
    if node:
        left = postorder(node.left, second_last_level_nodes, truth)
        right = postorder(node.right, second_last_level_nodes, truth)
        # If node not traversed, then add it
        if left and right:
            if node.data not in second_last_level_nodes:
                second_last_level_nodes[node.data].append(node)
            else:
                # If node with same data is found again, then check for equal subtrees for all node
                # with the given data
                for similar_node in second_last_level_nodes[node.data]:
                    # The node should not be a leaf
                    if (node.left or node.right):
                        truth[0] = truth[0] or compare_height_2_sub(similar_node, node)
    return isLeaf(node)

# We will traverse the tree in inorder fashion and if we encounter an already
# traversed node then, we check if it is equal subtree or not
def dupSub(node):
    """Function to find duplicate subtrees are present or not"""
    second_last_level_nodes = defaultdict(list)
    truth = [False]
    postorder(node, second_last_level_nodes, truth)
    return int(truth[0])

