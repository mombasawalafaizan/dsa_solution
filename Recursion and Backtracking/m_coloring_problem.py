#User function Template for python3
def isFeasible(u, V, adj_u, visited, color):
    for j in range(V):
        if adj_u[j]==1 and visited[j] and color[u]==color[j]:
            return False
    return True
    
def DFS(u, graph, k, V, visited, colored):
    visited[u] = True
    for color_possib in range(k):
        colored[u] = color_possib
        if isFeasible(u, V, graph[u], visited, colored):
            possible = True
            for adj_u in range(V):
                if graph[u][adj_u]==1 and visited[adj_u]==False:
                    if DFS(adj_u, graph, k, V, visited, colored)==False:
                        possible = False
                        break
            if possible:
                return True                        
    visited[u] = False
    return False
        
def graphColoring(graph, k, V):
    '''
    :param graph: grid of size V*V in specified format(0 based indexing i.e. vertex 1 is index 0)
    :param k: number of colors allowed
    :param V: number of vertices 
    :return: True or False
    '''
    #your code here
    visited = [False] * V
    colored = [-1] * V
    # print(graph)
    ans = True
    for i in range(V):
        if not visited[i]:
            ans = ans and DFS(i, graph, k, V, visited, colored)
    return ans