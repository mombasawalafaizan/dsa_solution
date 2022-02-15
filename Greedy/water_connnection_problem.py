# This is a graph
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0, 0] for _ in range(self.V + 1)]

    def addEdge(self, u, v, w):
        self.graph[u][0] = v
        self.graph[u][1] = w

    def DFSUtil(self, u, last):
        pipe_dia = 10 ** 6
        if self.graph[u][0] != 0:
            pipe_dia = min(self.graph[u][1], self.DFSUtil(self.graph[u][0], last))
        else:
            last[0] = u
        return pipe_dia

    def DFS(self, tanks):
        min_connections = 0
        ans = []
        for i in range(1, self.V + 1):
            if tanks[i] == 1 and self.graph[i][0] != 0:
                last = [-1]
                min_connections += 1
                min_pipe_dia = self.DFSUtil(i, last)
                ans.append([i, last[0], min_pipe_dia])
        print(min_connections)
        for i in ans:
            print(i[0], i[1], i[2])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        g = Graph(n)
        tanks = [0] * (n + 1)

        for q in range(p):
            u, v, w = map(int, input().split())
            g.addEdge(u, v, w)
            tanks[u] += 1
            tanks[v] += 1
        g.DFS(tanks)
