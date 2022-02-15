# O(n) space solution
def editDistance(s, t):
    # Code here
    dp = [i for i in range(len(s) + 1)]
    for i in range(len(t)):
        prev = dp[0]
        dp[0] = i + 1
        for j in range(1, len(s) + 1):
            temp = dp[j]
            if t[i] == s[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(dp[j], dp[j - 1], prev)
            prev = temp

    return dp[len(s)]
