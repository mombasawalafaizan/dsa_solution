# Given an array cost[] of positive integers of size N and an integer W, cost[i] represents the cost
# of ‘i’ kg packet of oranges, the task is to find the minimum cost to buy W kgs of oranges. If it 
# is not possible to buy exactly W kg oranges then the output will be -1

# NOTE:
# 1. cost[i] = -1 means that ‘i’ kg packet of orange is unavailable
# 2. It may be assumed that there is infinite supply of all available packet types.

# Input: N = 5, arr[] = {20, 10, 4, 50, 100}
# W = 5
# Output: 14
# Explanation: choose two oranges to minimize 
# cost. First orange of 2Kg and cost 10. 
# Second orange of 3Kg and cost 4.

def minimumCost(cost, N, W):
		# code here
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(1, W+1):
        dp[0][i] = 10**9
    
    last = 0
    for i in range(1, N+1):
        if cost[i-1] == -1:
            continue
        for j in range(1, W+1):
            if j < i:
                dp[i][j] = dp[last][j]
                continue
            dp[i][j] = min(dp[last][j], dp[i][j-i] + cost[i-1])
        last = i
    
    return dp[last][W] if dp[last][W]!=10**9 else -1

arr = [20, 10, 4, 50, 100]
print(minimumCost(arr, len(arr), 5))