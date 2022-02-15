# DP solution
def maxSubArraySum(arr,size):
    ##Your code here
    dp = [0] * size
    dp[0] = arr[0]
    max_so_far = arr[0]
    for i in range(size):
        dp[i] = max(arr[i]+dp[i-1], arr[i])
        max_so_far = max(dp[i], max_so_far)
        
    return max_so_far


# Space optimized DP solution
def maxSubArraySum(arr,size):
    ##Your code here
    curr_max = arr[0]
    max_so_far = arr[0]
    for i in range(size):
        curr_max = max(arr[i]+curr_max, arr[i])
        max_so_far = max(curr_max, max_so_far)
        
    return max_so_far