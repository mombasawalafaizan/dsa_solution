
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def DFS(self, real_node, vis):
        if real_node == None:
            return None
        clone = Node(real_node.val, [])
        vis[real_node.val] = clone
        for adj in real_node.neighbors:
            if adj.val not in vis:
                clone.neighbors.append(self.DFS(adj, vis))
            else:
                clone.neighbors.append(vis[adj.val])
        return clone
    
    def cloneGraph(self, node: Node) -> Node:
        vis = dict()
        return self.DFS(node, vis)