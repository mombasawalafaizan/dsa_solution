def equalPartition(arr):
    # code here
    N = len(arr)
    arr_sum = sum(arr)
    if arr_sum % 2 != 0:
        return 0
    dp = [[False] * (arr_sum + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True
    for i in range(1, N + 1):
        for j in range(1, arr_sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            print(int(dp[i][j]), end=" ")
        print()
    return int(dp[N][arr_sum // 2])


print(equalPartition([1, 5, 11, 5]))
