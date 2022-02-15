def findMaxSumNo3Consecutive(arr, n):
    dp = [0] * n
    if n>=1:
        dp[0] = arr[0]
    if n>=2:
        dp[1] = arr[1] + arr[0]
    if n>=3:
        dp[2] = max(dp[1], arr[0] + arr[2], arr[1]+arr[2])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3] + arr[i] + arr[i-1])
    return dp[n-1]


def FindMaxSumNo2Consecutive(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    # code here
    dp = [0] * n
    if n>=1:
        dp[0] = a[0]
    if n>=2:
        dp[1] = max(a[1], a[0])
    for i in range(2, n):
        dp[i] = max(a[i] + dp[i-2], dp[i-1])
    return dp[n-1]