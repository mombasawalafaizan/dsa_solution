# This code is accepted by GFG
def countWays(N, S):
    # code here
    n = N//2+1
    mod = 1003
    sym = [''] * (n-1)
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    k = 0
    for i in range(1,N,2):
        sym[k] = S[i]
        k += 1
    k = 0
    for i in range(0, N, 2):
        if S[i] == 'T':
            dp[k][k][0] = 1
        else:
            dp[k][k][1] = 1
        k += 1
        
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            for k in range(i, j):
                temp = [0, 0]
                if sym[k] == '&':
                    temp[0] = (dp[i][k][0] * dp[k+1][j][0])%mod
                    temp[1] = ((dp[i][k][1] * dp[k+1][j][0])%mod + (dp[i][k][1] * dp[k+1][j][1])%mod + (dp[i][k][0] * dp[k+1][j][1])%mod)%mod
                elif sym[k] == '|':
                    temp[0] = ((dp[i][k][0] * dp[k+1][j][0])%mod + (dp[i][k][0] * dp[k+1][j][1])%mod + (dp[i][k][1] * dp[k+1][j][0])%mod)%mod
                    temp[1] = (dp[i][k][1] * dp[k+1][j][1])%mod
                else:
                    temp[0] = ((dp[i][k][0] * dp[k+1][j][1])%mod + (dp[i][k][1] * dp[k+1][j][0])%mod)%mod
                    temp[1] = ((dp[i][k][0] * dp[k+1][j][0])%mod + (dp[i][k][1] * dp[k+1][j][1])%mod)%mod
                dp[i][j][0] = (dp[i][j][0] + temp[0])%mod
                dp[i][j][1] = (dp[i][j][1] + temp[1])%mod
    return dp[0][n-1][0]


# Same as above solution and time complexity, but with more clarity
class Truth:
    def __init__(self):
        self.T = 0
        self.F = 0

def merge(a, b, x):
    ans = Truth()
    if x == '&':
        ans.T = a.T * b.T
        ans.F = a.F * b.T + a.F * b.F + a.T * b.F
    elif x == '|':
        ans.T = a.T * b.T + a.T * b.F + a.F * b.T
        ans.F = a.F * b.F
    else:
        ans.T = a.T * b.F + a.F * b.T
        ans.F = a.T * b.T + a.F * b.F
    return ans


def countWaysEasyUnderstand(N, S):
    n = N//2+1
    sym = [''] * (n-1)
    dp = [[Truth() for _ in range(n)] for _ in range(n)]
    k = 0
    for i in range(1,N,2):
        sym[k] = S[i]
        k += 1
    k = 0
    for i in range(0, N, 2):
        if S[i] == 'T':
            dp[k][k].T = 1
        else:
            dp[k][k].F = 1
        k += 1
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            for k in range(i, j):
                temp = merge(dp[i][k], dp[k+1][j], sym[k])
                dp[i][j].T += temp.T
                dp[i][j].F += temp.F
    return dp[0][n-1].T

S = 'T|T&F^T'
countWaysEasyUnderstand(len(S), S)