# DP solution
def minSubArraySum(arr,size):
    ##Your code here
    dp = [0] * size
    dp[0] = arr[0]
    min_so_far = arr[0]
    for i in range(size):
        dp[i] = min(arr[i]+dp[i-1], arr[i])
        min_so_far = min(dp[i], min_so_far)
        
    return min_so_far


# Space optimized DP solution
def minSubArraySum1(arr,size):
    ##Your code here
    curr_min = arr[0]
    min_so_far = arr[0]
    for i in range(size):
        curr_min = min(arr[i]+curr_min, arr[i])
        min_so_far = min(curr_min, min_so_far)
        
    return min_so_far

arr = [2, 6, 8, 1, 4]
print(minSubArraySum1(arr, len(arr)))