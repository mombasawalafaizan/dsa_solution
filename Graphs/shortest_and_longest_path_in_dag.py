from collections import deque, defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.edges = []

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.edges.append([u, v, w])

# Using DFS type approach
def topoSortUtil(v, visited, stack, graph):
    visited[v] = True
    for adj in graph[v]:
        if visited[adj[0]] == False:
            topoSortUtil(adj[0], visited, stack, graph)
    stack.append(v) # This is the only additional line than DFS algorithm
    
def topoSort(n, adj):
    visited = [False] * n
    stack = deque()
    for i in range(n):
        if visited[i]==False:
            topoSortUtil(i, visited, stack, adj)
    return stack

def longestPath(n, graph, s):
    dist = [float('-inf')]*n
    dist[s] = 0
    stack = topoSort(n, graph)
    # print(stack)
    while stack:
        u = stack.pop()
        if dist[u] != float('-inf'):
            for v in graph[u]:
                # If we reverse the comparator, this will become the
                # shortest path from source in a directed acyclic graph
                if (dist[u] + v[1]) > dist[v[0]]:
                    dist[v[0]] = (dist[u] + v[1])
    return dist

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0, 1, 5)  
    g.addEdge(0, 2, 3)  
    g.addEdge(1, 3, 6)  
    g.addEdge(1, 2, 2)  
    g.addEdge(2, 4, 4)  
    g.addEdge(2, 5, 2)  
    g.addEdge(2, 3, 7)  
    g.addEdge(3, 5, 1)  
    g.addEdge(3, 4, -1)  
    g.addEdge(4, 5, -2)
    print(longestPath(g.V, g.graph, 1))