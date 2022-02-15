# Kosaraju's algorithm
from collections import defaultdict, deque

def DFSUtil(u, vis, g):
    vis[u] = True
    for adj in g[u]:
        if not vis[adj]:
            DFSUtil(adj, vis, g)
            
def fillOrder(u, vis, stack, g):
    vis[u] = True
    for adj in g[u]:
        if not vis[adj]:
            fillOrder(adj, vis, stack, g)
    stack.append(u)

def countSCCs (adj, V):
    g = defaultdict(list)
    for i in range(0, len(adj), 2):
        g[adj[i]].append(adj[i+1])
    # print(g)
    stack = deque()
    vis = [False] * V
    for u in range(V):
        if not vis[u]:
            fillOrder(u, vis, stack, g)
    
    gT = defaultdict(list)
    for i in range(0, len(adj), 2):
        gT[adj[i+1]].append(adj[i])
    print(gT)
    vis = [False] * V
    sccs = 0
    while stack:
        i = stack.pop()
        if vis[i]==False:
            DFSUtil(i, vis, gT)
            sccs += 1
    return sccs

adj = '1 0 0 2 2 1 0 3 3 4'
edges = list(map(int, adj.split()))
print(countSCCs(edges, 5))