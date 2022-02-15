# If it is allowed to rearrange the pairs, then this is
# the simple Activity Selection Problem

def maxChainLen(Parr, n):
    # Parr:  list of pair
    #code here
    Parr.sort(key = lambda x: x.b)
    res = 1
    idx = 0
    for i in range(1, n):
        if Parr[i].a > Parr[idx].b:
            res += 1
            idx = i
    return res

# This is DP solution like Longest Increasing Subsequence,
# in which we construct chain using subsequence
# Time: O(n^2) Space: O(n)
def maxChainLen(Parr, n):
    dp = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if Parr[j].a > Parr[i].b:
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)
