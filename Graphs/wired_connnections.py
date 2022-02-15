from queue import Queue
from collections import defaultdict
from typing import List

class Solution:
    def findExtraEdges(self, s, vis, graph):
        edges = 0
        nodes = 0
        q = Queue()
        q.put(s)
        vis[s] = True
        while not q.empty():
            cur = q.get()
            edges += len(graph[cur])
            for adj in graph[cur]:
                if not vis[adj]:
                    q.put(adj)
                    vis[adj] = True
                    nodes += 1
                    
        return edges//2 - nodes
        
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n-1):
            return -1
        graph = defaultdict(list)
        for con in connections:
            graph[con[0]].append(con[1])
            graph[con[1]].append(con[0])
        vis = [False] * n
        groups = 0
        extra_edges = 0
        for i in range(n):
            if not vis[i]:
                if i in graph:
                    extra_edges += self.findExtraEdges(i, vis, graph)
                groups += 1
                
        if (groups-1)>extra_edges:
            return -1
        else:
            return groups-1


# A beautiful solution
def makeConnected1(n, connections):
    if len(connections) < n - 1: return -1
    G = [[] for i in range(n)]
    for i, j in connections:
        G[i].append(j)
        G[j].append(i)
    seen = [False] * n
    def dfs(i):
        if seen[i]: return 0
        seen[i] = True
        for j in G[i]: dfs(j)
        return 1

    return sum(dfs(i) for i in range(n)) - 1

connections = [[0, 1], [0, 2], [1, 2], [3, 4]]
print(makeConnected1(5, connections))