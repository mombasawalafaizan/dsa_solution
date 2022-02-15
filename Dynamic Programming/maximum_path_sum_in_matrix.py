# This is same as Gold Mine problem, this is just asked for rows,
# logic is same
# NOTE: I have implemented optimized space version of goldmine problem here
# Time complexity: O(n*n) Space complexity: O(n)
def maximumPath(N, mat):
        # code here
    dp = [[0 for _ in range(N)] for _ in range(2)]
    for i in range(N):
        dp[0][i] = mat[0][i]
        
    bi = 0
    for i in range(1, N):
        bi = i&1
        for j in range(N):
            left = dp[1-bi][j-1] if j > 0 else 0
            right = dp[1-bi][j+1] if j < N-1 else 0
            dp[bi][j] = mat[i][j] + max(dp[1-bi][j], left, right)
    return max(dp[bi])