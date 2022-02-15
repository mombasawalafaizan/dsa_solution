#code
def floyd_warshall(graph, v):
    dist = graph.copy()  # Make the dist 
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], 
                    dist[i][k] + dist[k][j])
    return dist
    
if __name__ == '__main__':
    v = 3
    # Matrix can be directed or undirected
    matrix = [[0, 1, 43],
            [1, 0, 6],
            [43, 6, 0]]
    all_pairs = floyd_warshall(matrix, v)
    for i in range(v):
        for j in all_pairs[i]:
            if j==float('inf'):
                print('INF', end=' ')
            else:
                print(j, end=' ')
        print()