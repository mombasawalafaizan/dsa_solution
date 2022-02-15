from collections import defaultdict, deque
class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])
    
    def _DFSUtil(self, s, k, vis, path):
        if k <= 0:
            return True
        for i in self.graph[s]:
            if vis[i[0]] == False:
                vis[i[0]] = True
                if self._DFSUtil(i[0], k-i[1], vis, path):
                    path.appendleft(i[0])
                    return True
                vis[i[0]] = False
        return False            

    def pathMoreThanK(self, s, k):
        vis = [False] * self.V
        vis[s] = True
        path = deque()
        if self._DFSUtil(s, k, vis, path)==False:
            print('No solution exists')
        else:
            path.appendleft(s)
            for i in path:
                print(str(i)+' ->', end=' ')
            print('END')


if __name__ == "__main__":
    g = Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(7, 8, 7)
    g.addEdge(7, 6, 1)
    g.addEdge(8, 6, 6)
    g.addEdge(2, 8, 2)
    g.addEdge(1, 2, 8)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 5, 4)
    g.addEdge(6, 5, 2)
    g.addEdge(3, 5, 14)
    g.addEdge(5, 4, 10)
    g.addEdge(3, 4, 9)
    g.pathMoreThanK(0, 61)