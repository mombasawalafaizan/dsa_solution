def longestCommonSubstr(S1, S2, n, m):
        # code here
    dp  = [[0 for _ in range(m+1)] for _ in range(n+1)]
    max_len = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if S1[i-1] == S2[j-1]: 
                # If there is a preceding ongoing substring
                if i>1 and j>1 and S1[i-2]==S2[j-2]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                # If a single character or no preceding substring 
                else: 
                    dp[i][j] = 1
                if dp[i][j] > max_len: max_len = dp[i][j]
                
    return max_len 