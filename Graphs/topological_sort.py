from collections import deque, defaultdict

# Using DFS type approach
def topoSortUtil(v, visited, stack, graph):
    visited[v] = True
    for adj in graph[v]:
        if visited[adj] == False:
            topoSortUtil(adj, visited, stack, graph)
    stack.appendleft(v)  # This is the only additional line than DFS algorithm


def topoSort1(n, adj):
    # visited = [False] * n
    visited = dict()
    for i in n:
        visited[i] = False
    stack = deque()
    # for i in range(n):
    #     if visited[i]==False:
    #         topoSortUtil(i, visited, stack, adj)
    for i in n:
        if visited[i] == False:
            topoSortUtil(i, visited, stack, adj)
    return stack


def addEdge(graph, u, v):
    graph[u].append(v)


if __name__ == "__main__":
    graph = defaultdict(list)
    addEdge(graph, "r", "t")
    addEdge(graph, "r", "s")
    addEdge(graph, "t", "y")
    addEdge(graph, "t", "z")
    addEdge(graph, "t", "x")
    addEdge(graph, "x", "y")
    addEdge(graph, "x", "z")
    addEdge(graph, "s", "x")
    addEdge(graph, "s", "t")
    addEdge(graph, "y", "z")
    print(topoSort1(["r", "s", "t", "x", "y", "z"], graph))


# Using Kahn's algorithm (Source removal technique)
def topoSort2(n, adj):
    in_degree = [0] * n
    for i in adj:
        for j in adj[i]:
            in_degree[j] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    cnt = 0
    top_order = []
    while queue:
        u = queue.popleft()
        top_order.append(u)
        for i in adj[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
        cnt += 1
    return top_order
