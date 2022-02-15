# My DP solution   Time: O(nlogn) Space: O(n)
def pairsWithDifference(arr, N, K):
    arr.sort()
    max_sum = arr[0]
    dp = [0] * N
    for i in range(1, N):
        max_sum += arr[i]
        if arr[i] < (arr[i-1]+K):
            dp[i] = dp[i-1]
        else:
            if (i-dp[i-1])%2!=0:
                max_sum -= arr[dp[i-1]]
            dp[i] = i
    if (N-dp[N-1])%2!=0:
        max_sum -= arr[dp[N-1]]
    return max_sum

# Optimized DP solution with O(1) space
def pairsWithDifference(arr, N, K):
    arr.sort()
    max_sum = arr[0]
    prev = 0
    for i in range(1, N):
        max_sum += arr[i]
        if arr[i] >= (arr[i-1]+K):
            if (i-prev)%2!=0:
                max_sum -= arr[prev]
            prev = i
            
    if (N-prev)%2!=0:
        max_sum -= arr[prev]
    return max_sum

# Another good solution with O(1) space and O(nlogn) time
def maxSumPairWithDifferenceLessThanK(arr, N, k):

    maxSum = 0

    # Sort elements to ensure every i and
    # i-1 is closest possible pair
    arr.sort()

    # To get maximum possible sum, iterate
    # from largest to smallest, giving larger
    # numbers priority over smaller numbers.
    i = N - 1
    while (i > 0):

        # Case I: Diff of arr[i] and arr[i-1]
        #     is less then K, add to maxSum
        # Case II: Diff between arr[i] and
        #     arr[i-1] is not less then K,
        #     move to next i since with sorting
        #     we know, arr[i]-arr[i-1] < arr[i]-arr[i-2]
        #     and so on.
        if (arr[i] - arr[i - 1] < k):

            # Assuming only positive numbers.
            maxSum += arr[i]
            maxSum += arr[i - 1]

            # When a match is found skip this pair
            i -= 1
        i -= 1

    return maxSum

# DP solution from GFG
# Python3 program to find maximum pair 
# sum whose difference is less than K
 
# method to return maximum sum we can 
# get by get by finding less than K
# difference pair
def maxSumPairWithDifferenceLessThanK(arr, N, K):
 
    # Sort input array in ascending order.
    arr.sort()
 
    # dp[i] denotes the maximum disjoint
    # pair sum we can achieve using first
    # i elements
    dp = [0] * N
 
    # if no element then dp value will be 0
    dp[0] = 0
 
    for i in range(1, N):
     
        # first give previous value to
        # dp[i] i.e. no pairing with
        # (i-1)th element
        dp[i] = dp[i-1]
 
        # if current and previous element 
        # can form a pair
        if (arr[i] - arr[i-1] < K):
         
            # update dp[i] by choosing
            # maximum between pairing
            # and not pairing
            if (i >= 2):
                dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1])
            else:
                dp[i] = max(dp[i], arr[i] + arr[i-1])
         
    # last index will have the result
    return dp[N - 1]
 
# Driver code to test above methods
arr = [3, 5, 10, 15, 17, 12, 9]
N = len(arr)
K = 4
print(maxSumPairWithDifferenceLessThanK(arr, N, K))
 