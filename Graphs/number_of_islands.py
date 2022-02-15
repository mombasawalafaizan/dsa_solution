#User function Template for python3
from collections import deque

def isSafe(A, i, j, N, M, vis):
    return (i>=0 and i<N and j>=0 and j<M and 
            vis[i][j]==False and A[i][j]==1)

def BFS(A, a, b, N, M, vis):
    row = [-1, -1, -1, 0, 0, 1, 1, 1]
    col = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = deque()
    q.append((a, b))
    vis[a][b] = True
    while len(q)!=0:
        i, j = q.popleft()
        # print(i, j)
        for k in range(8):
            if isSafe(A, i+row[k], j+col[k], N, M, vis):
                vis[i+row[k]][j+col[k]] = True
                q.append((i+row[k], j+col[k]))
    
def findIslands(A, N, M):
    founded = 0
    vis = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1 and vis[i][j] == False:
                # print(vis)
                BFS(A, i, j, N, M, vis)
                founded += 1
    return founded