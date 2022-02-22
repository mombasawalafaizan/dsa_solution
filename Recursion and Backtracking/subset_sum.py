# Recursive backtracking solution
def partUtil(arr, idx, part_1, part_2, n):
    if idx == n:
        if part_1 == part_2:
            print(part_1)
        return part_1 == part_2
    # Pick
    ans = False
    if part_1 <= part_2:
        ans = ans or partUtil(arr, idx + 1, part_1 + arr[idx], part_2, n)
    # Don't pick
    ans = ans or partUtil(arr, idx + 1, part_1, part_2 + arr[idx], n)
    return ans


def equalPartitionRecursive(self, N, arr):
    return int(partUtil(arr, 0, 0, 0, N))


# DP solution in O(n * sum(arr)) time and O(n * sum(arr)) space complexity
def equalPartitionDP(N, arr):
    arr_sum = sum(arr)
    if arr_sum % 2 != 0:
        return 0
    dp = [[0] * (arr_sum + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        for j in range(1, arr_sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                if dp[i][j]:
                    print(i, j, arr[i - 1], dp[i - 1][j - arr[i - 1]])
    for i in dp:
        print(i)
    return dp[N][arr_sum // 2]


arr = [5, 1, 11, 5]
N = 4
equalPartitionDP(N, arr)
