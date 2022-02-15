from typing import List
from bisect import bisect_left


def maxContiguousSum_K_POSITIVE(arr, k):
    # This function cannot handle negative numbers case
    n = len(arr)
    i = 0
    j = 1
    max_sum = -2**31
    curr_sum = arr[0]
    while i < n:
        if curr_sum <= k:
            max_sum = max(curr_sum, max_sum)

        if j < n and (i == j or curr_sum <= k):
            curr_sum += arr[j]
            j += 1
        else:
            curr_sum -= arr[i]
            i += 1

    return max_sum if max_sum != -2**31 else k+1


def maxContiguousSum_K(arr, k):
    cum_set = set()
    cum_set.add(0)
    max_sum = -10**9
    cSum = 0

    for i in range(len(arr)):
        cSum += arr[i]
        x = sorted(cum_set)
        sit = bisect_left(x, cSum - k)
        if sit < len(x):
            max_sum = max(max_sum, cSum - x[sit])
        cum_set.add(cSum)
    return max_sum


def maxSumSubmatrix(matrix: List[List[int]], k: int) -> int:
    R = len(matrix)
    C = len(matrix[0])
    prefix = [[0 for _ in range(C+1)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            prefix[i][j+1] = matrix[i][j] + prefix[i][j]

    rec_sum = [0] * R
    res = -10**9
    for right in range(1, C+1):
        for left in range(right):
            for i in range(R):
                rec_sum[i] = prefix[i][right] - prefix[i][left]
            res = max(res, maxContiguousSum_K(rec_sum, k))
    return res


# matrix = [[2, 2, -1]]
# k = 0
# print(maxSumSubmatrix(matrix, k))
