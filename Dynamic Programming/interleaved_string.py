def isInterleave(A, B, C):
    # Code here
    n1 = len(A)
    n2 = len(B)
    if len(C) != (n1 + n2):
        return False
    dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1+1):
        for j in range(n2+1):
            if i==0 and j==0:
                dp[i][j] = True
                
            elif i==0:
                if B[j-1]==C[j-1]: dp[i][j] = dp[i][j-1]
                
            elif j==0:
                if A[i-1]==C[i-1]: dp[i][j] = dp[i-1][j]
                
            elif A[i-1]==C[i+j-1] and B[j-1]!=C[i+j-1]:
                dp[i][j] = dp[i-1][j]
            
            elif A[i-1]!=C[i+j-1] and B[j-1]==C[i+j-1]:
                dp[i][j] = dp[i][j-1]
            
            elif A[i-1]==C[i+j-1] and B[j-1]==C[i+j-1]:
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            
    return dp[n1][n2]