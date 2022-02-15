from queue import Queue
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    vis = [False]*n
    parent = [-1] * n
    q = Queue()
    for u in g:
        if not vis[u]:
            q.put(u)
            vis[u] = True
            while not q.empty():
                cur_node = q.get()
                for adj in g[cur_node]:
                    if not vis[adj]:
                        vis[adj] = True
                        parent[adj] = cur_node
                        q.put(adj)
                    elif parent[cur_node]!=adj:
                        return 1
    return 0

# DFS approach
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    vis = [False]*n
    for u in g:
        if not vis[u]:
            if _dfs_helper(g, u, vis, -1):
                return 1
    return 0
            
def _dfs_helper(g, u, vis, parent):
    vis[u] = True
    for adj in g[u]:
        if not vis[adj]:
            if _dfs_helper(g, adj, vis, u):
                return True
        elif parent!=adj:
            return True
    return False