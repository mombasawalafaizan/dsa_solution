from collections import deque
def isBipartite(arr, n):
    # Code here
    q = deque()
    src = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                src = i
                break
    # Use this as color set or use 0-1 array then you have to only subtract
    # color_set = [-1] * n
    # color_set[src]=1
    color_set = [' '] * n
    color_set[src] = 'R'
    q.append(src)
    while q:
        node = q.popleft()
        for adj in range(n):
            if arr[node][adj] == 1:
                # If self loop or adjacent have same colors
                if adj==node or color_set[adj] == color_set[node]:
                    return False
                if color_set[adj]==' ':
                    color_set[adj] = 'B' if color_set[node] == 'R' else 'R'
                    q.append(adj)
                # if color_set[adj]==-1:
                #     color_set[adj] = 1-color_set[node]
                #     q.append(adj)
                
    return True

arr = [[0,  1, 0,  1], [1, 0,  1, 0],  [0,  1, 0,  1], [1, 0,  1, 0] ]
n = 4
print(isBipartite(arr, n))