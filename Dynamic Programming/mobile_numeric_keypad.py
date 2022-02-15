def getCount(self, N):
    # code here
    keypad = [(0, 8), (1, 2, 4), (1, 2, 3, 5), (2, 3, 6), (1, 4, 5, 7), (2, 4, 5, 6, 8), 
        (3, 5, 6, 9), (4, 7, 8), (5, 7, 8, 9, 0), (6, 8, 9)]
    dp = [1] * 10
    for i in range(2, N+1):
        temp = [0] * 10
        for i in range(10):
            for k in keypad[i]:
                temp[i] += dp[k]
        dp = temp[:]
        
    return sum(dp)