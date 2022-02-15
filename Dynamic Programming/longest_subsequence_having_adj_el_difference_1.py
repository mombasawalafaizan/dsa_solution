def longestSubsequence(self, n, arr):
    # code here
    dp = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if abs(arr[j] - arr[i]) == 1:
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)
