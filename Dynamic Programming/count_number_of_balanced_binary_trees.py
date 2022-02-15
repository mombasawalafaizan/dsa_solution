def countBT (self, h):
        # code here 
        # mod = 10**9 + 7
        dp = [1] * (h+1)
        for i in range(2, h+1):
            dp[i] = dp[i - 1] * (2 * dp [i - 2] + dp[i - 1])  
            # dp[i] = (dp[i - 1] * ((2 * dp [i - 2])% mod + dp[i - 1]) % mod) % mod
        return dp[h]