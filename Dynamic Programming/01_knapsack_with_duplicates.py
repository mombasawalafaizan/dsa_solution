def knapSack(W, wt, val, n):
    """
    :param W: capacity of knapsack
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    """
    # code here
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j - wt[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - wt[i - 1]] + val[i - 1])
    return dp[n][W]


def knapSackDuplicates(N, W, val, wt):
    # code here
    dp = [0 for _ in range(W + 1)]

    for i in range(N + 1):
        for j in range(wt[i - 1], W + 1):
            dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])
    return dp[W]
