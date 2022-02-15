def maxSquare(n, m, mat):
        # code here
    dp = [[0 for _ in range(m)] for _ in range(n)]
    max_size = 0
    for i in range(n):
        dp[i][0] = mat[i][0]
        
    for j in range(m):
        dp[0][j] = mat[0][j]
        
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j]==1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = 0
    
    max_size = 0
    for i in range(n):
        for j in range(m):
            if max_size < dp[i][j]:
                max_size = dp[i][j]
    for i in dp:
        print(i)
    
    return max_size

mat = [
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
print(maxSquare(len(mat), len(mat[0]), mat))