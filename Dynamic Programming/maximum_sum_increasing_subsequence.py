# DP solution Time complexity: O(n^2) Space complexity: O(n)
def maxSumIS(self, arr, n):
    # code here
    dp = arr[:]
    for i in range(n-2, -1, -1):
        temp = 0
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                temp = max(temp, dp[j])  
        dp[i] += temp
    return max(dp)