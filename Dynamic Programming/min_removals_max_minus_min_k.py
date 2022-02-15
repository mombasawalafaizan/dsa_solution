from bisect import bisect_right

# This uses time: O(nlogn) and O(1) space
def minRemove(arr, n, k):
    arr.sort()
    min_remove = n - 1
    for i in range(n):
        idx = bisect_right(arr, arr[i] + k)
        min_remove = min(min_remove, n - (idx - i))
    return min_remove


# This uses time: O(nlogn) for sorting and O(n) for solution and O(n) space
# More optimized version using DP
# As outer loop is going to make n interations. And the inner loop iterates at max n times for all
# outer iterations. Because we start value of j from dp[i-1] and loops it until it reaches i and
# then for the next element we again start from the previous dp[i] value. So the total time complexity
# is O(n) if we don’t consider the complexity of the sorting as it is not considered in the above solution
# as well.


def minRemoveDP(arr, n, k):
    arr.sort()
    dp = [-1] * n
    dp[0] = 0
    min_remove = n - 1
    for i in range(1, n):
        dp[i] = i
        j = dp[i - 1]
        while j != i and (arr[j] - arr[i] > k):
            j += 1
        dp[i] = min(dp[i], j)
        min_remove = min(min_remove, n - (i - j + 1))
    return min_remove


def minRemoveNoSpace(arr, n, k):
    arr.sort()
    min_idx = 0
    min_remove = n - 1
    for i in range(1, n):
        j = min_idx
        while j != i and (arr[j] - arr[i] > k):
            j += 1
        min_idx = min(i, j)
        min_remove = min(min_remove, n - (i - j + 1))
    return min_remove
