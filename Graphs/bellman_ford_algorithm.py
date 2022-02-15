def bellman_ford(edges, V):
    dist = [float('inf')] * V
    src = edges[0][0]
    dist[src] = 0
    
    for _ in range(V-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and (dist[u] + w) < dist[v]:
                dist[v] = (dist[u] + w)
    
    # This loop is for detection of negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and (dist[u] + w) < dist[v]:
            return []
    # If no cycle return dist list
    return dist
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        V, E = map(int, input().split())
        temp = list(map(int, input().split()))
        edges = []
        for i in range(0, len(temp), 3):
            edges.append([temp[i], temp[i+1], temp[i+2]])
        # print(edges)
        print(int(bellman_ford(edges, V)))