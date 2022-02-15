# Such path is called Euler Path
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def rmvEdge(self, u, v):
        for i in range(len(self.graph[u])):
            if self.graph[u][i] == v:
                self.graph[u][i] = -1

        for i in range(len(self.graph[v])):
            if self.graph[v][i] == u:
                self.graph[v][i] = -1
            
def printEulerTour(g):
    u = -1
    cnt = 0
    for i in range(g.V):
        if len(g.graph[i])%2!=0:
            cnt += 1
            if u == -1:
                u = i
    u = 0 if u == -1 else u
    if cnt <= 2:
        printEulerUtil(u, g)
    else:
        print('Not possible', end='')
    print()

def printEulerUtil(u, g):
    for v in g.graph[u]:
        if v!=-1 and isValidNextEdge(u, v, g):
            print(u,'-',v,end=' ')
            g.rmvEdge(u, v)
            printEulerUtil(v, g)

def isValidNextEdge(u, v, g):
    cnt = 0
    for i in g.graph[u]:
        if i!=-1: cnt+=1
    if cnt==1: return True

    vis = [False] * g.V
    count1 = DFSCount(u, vis, g)
    g.rmvEdge(u, v)

    vis = [False] * g.V
    count2 = DFSCount(u, vis, g)
    g.addEdge(u, v)
    return count1 <= count2

def DFSCount(u, vis, g):
    vis[u] = True
    count = 1
    for adj in g.graph[u]:
        if adj!=-1 and not vis[adj]:
            count += DFSCount(adj, vis, g)
    return count

if __name__ == "__main__":
    g1  = Graph(4)
    g1.addEdge(0, 1) 
    g1.addEdge(0, 2) 
    g1.addEdge(1, 2) 
    g1.addEdge(2, 3)
    printEulerTour(g1)

    g3 = Graph(4)
    g3.addEdge(0, 1) 
    g3.addEdge(0, 2) 
    g3.addEdge(2, 3) 
    g3.addEdge(3, 1)
    printEulerTour(g3)

