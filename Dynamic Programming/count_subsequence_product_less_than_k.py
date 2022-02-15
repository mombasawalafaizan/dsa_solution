# Python3 program to find
# number of subarrays having
# product less than k.
def productSubSeqCount(arr, k):
    n = len(arr)
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
    # print(dp[0])
    for i in range(1, k + 1):
        # print("{t: 3d} |".format(t=i), end=" ")
        for j in range(1, n + 1):

            # number of subsequence
            # using j-1 terms
            dp[i][j] = dp[i][j - 1]

            # if arr[j-1] > i it will
            # surely make product greater
            # thus it won't contribute then
            if arr[j - 1] <= i and arr[j - 1] > 0:

                # number of subsequence
                # using 1 to j-1 terms
                # and j-th term
                dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
            # print("{t: 2d}".format(t=dp[i][j]), end=" ")
        # print()
    return dp[k][n]


# Driver code
A = [1, 2, 3, 4]
k = 10
print(productSubSeqCount(A, k))
