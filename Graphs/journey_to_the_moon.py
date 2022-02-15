from collections import defaultdict, deque

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    class Graph:
        def __init__(self, V):
            self.V = V
            self.graph = defaultdict(list)
        
        def addEdge(self, u, v):
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        def calculatePairs(self, arr: list) -> int:
            """i = len(arr) - 2
            sum_arr = arr[:]
            for i in range(len(arr)-2, -1, -1):
                sum_arr[i] = sum_arr[i] + sum_arr[i+1]"""
            sum = arr[-1]
            pairs = 0
            for i in range(len(arr) - 2, -1, -1):
                pairs += arr[i] * sum
                sum += arr[i]
            return pairs


        def BFS(self):
            visited = [False] * self.V
            queue = deque()
            nodes = []
            for i in range(self.V):
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    cnt = 1
                    while queue:
                        v = queue.popleft()
                        if v in self.graph: # If v is not a single node
                            for j in self.graph[v]: # Every adjacent node of v
                                if visited[j] == False:
                                    visited[j] = True
                                    queue.append(j)
                                    cnt += 1
                        else:
                            visited[v] = True
                    nodes.append(cnt)
            return self.calculatePairs(nodes)

    g = Graph(n)
    for a, b in astronaut:
        g.addEdge(a, b)
    return g.BFS()