from collections import defaultdict
import heapq
class Pair:
    def __init__(self, w, u):
        self.w = w
        self.u = u 

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])

    # Dijkstra's shortest path
    def shortestPath(self, src, dst): 
        heap=[(0, src)]
        while heap:
            cur_dist, u = heapq.heappop(heap)
            if u == dst:
                return cur_dist
            for adj in self.graph[u]:
                heapq.heappush(heap, (cur_dist + adj[1], adj[0]))
        return -1

def modelGraphWithEdgeWeight(edge, E, V):
    g = Graph(V)
    for i in range(E):
        g.addEdge(edge[i][0], edge[i][1], 0)
        g.addEdge(edge[i][1], edge[i][0], 1)
    return g

def minEdgeReverse(edges, E, V, src, dest):
    g = modelGraphWithEdgeWeight(edges, E, V)
    dist = g.shortestPath(src, dest)
    return dist

if __name__ == "__main__":
    edges = [ [ 0, 1 ], [ 2, 1 ],
                     [ 2, 3 ], [ 5, 1 ], 
                     [ 4, 5 ], [ 6, 4 ], 
                     [ 6, 3 ] ]
    E = len(edges)
    V = 7
    print(minEdgeReverse(edges, E, V, 0, 6))