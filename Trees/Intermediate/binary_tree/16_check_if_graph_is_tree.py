from collections import defaultdict, deque
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Check for cycles and make sure all nodes are visited
    def checkTree(self, s):
        visited = {x: False for x in self.graph}
        parent = {x: -1 for x in self.graph}
        queue = deque()
        parent[s] = None
        visited[s] = True
        queue.append(s)

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                elif parent[u] != v:
                    return False

        return True and not any(visited.values()) 