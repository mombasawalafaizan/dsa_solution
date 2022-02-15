from collections import deque

# DFS cycle 
def dfs_cycle(graph, node, onpath, visited):
    if visited[node]:
        return False
    onpath[node] = visited[node] = True
    for adj in graph[node]:
        if onpath[adj] or dfs_cycle(graph, adj, onpath, visited):
            return True
    onpath[node] = False
    return False

def canFinishDFS(numtasks, tasks):
    graph = {i: [] for i in range(numtasks)}
    for task in tasks:
        graph[task[1]].append(task[0])
    onpath = [False] * numtasks
    visited = [False] * numtasks
    for i in range(numtasks):
        if not visited[i] and dfs_cycle(graph, i, onpath, visited):
            return False
    return True

# BFS-based approach using topological sorting concept
def canFinishBFS(numtasks, tasks):
    graph = {i: [] for i in range(numtasks)}
    for task in tasks:
        graph[task[1]].append(task[0])
    in_degree = [0] * numtasks
    for i in graph:
        for j in graph[i]:
            in_degree[j] += 1
    
    for i in range(numtasks):
        j = 0
        while j < numtasks:
            if in_degree[j] == 0:
                break
            j += 1
        if j == numtasks:
            return False
        in_degree[j] = -1
        for adj in graph[j]:
            in_degree[adj] -= 1

    return True 

if __name__ == "__main__":
    numtasks=4
    tasks = [[1, 0], [2, 1], [3, 2]]
    # numtasks=2
    # tasks = [[1, 0], [0, 1]]
    # if canFinishBFS(numtasks, tasks):
    #     print('Possible to finish')
    if canFinishDFS(numtasks, tasks):
        print('Possible to finish')
    else:
        print('Impossible to finish')