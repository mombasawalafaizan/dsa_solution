# Let profit[t][i] represent maximum profit using at most t transactions up to day i (including day i). 
# Then the relation is:
# profit[t][i] = max(profit[t][i-1], max(A[i] – A[j] + profit[t-1][j])) 
#           for all j in range [0, i-1] 
# profit[t][i] will be maximum of – 

# 1) profit[t][i-1] which represents not doing any transaction on the ith day.
# 2) Maximum profit gained by selling on ith day. In order to sell shares on ith day, 
#    we need to purchase it on any one of [0, i – 1] days. 
#    If we buy shares on jth day and sell it on ith day, 
#    max profit will be A[i] – A[j] + profit[t-1][j] where j varies from 0 to i-1. 
#    Here profit[t-1][j] is best we could have done with one less transaction till jth day.

# This is the O(k*n^2) time complexity solution
def maxProfit(A, n, K):
    # code here
    profit = [[0 for _ in range(n)] for _ in range(K+1)]
    
    for i in range(1, n):
        for k in range(1, K+1):
            max_so_far = 0
            for j in range(i):
                max_so_far = max(max_so_far, A[i] - A[j] + profit[k-1][j])
            profit[k][i] = max(profit[k][i-1], max_so_far)
    return profit[K][n-1]

# The above solution has time complexity of O(k.n2). It can be reduced if we are able to calculate the maximum profit gained by selling shares on the ith day in constant time.
# profit[t][i] = max(profit [t][i-1], max(A[i] – A[j] + profit[t-1][j])) 
#                             for all j in range [0, i-1]
# If we carefully notice, 
# max(A[i] – A[j] + profit[t-1][j]) 
# for all j in range [0, i-1]
# can be rewritten as, 
# = A[i] + max(profit[t-1][j] – A[j]) 
# for all j in range [0, i-1] 
# = A[i] + max(prevDiff, profit[t-1][i-1] – A[i-1]) 
# where prevDiff is max(profit[t-1][j] – A[j]) 
# for all j in range [0, i-2]
# So, if we have already calculated max(profit[t-1][j] – A[j]) for all j in range [0, i-2], 
# we can calculate it for j = i – 1 in constant time. In other words, we don’t have to look back 
# in the range [0, i-1] anymore to find out best day to buy. We can determine that in constant time 
# using below revised relation.
# profit[t][i] = max(profit[t][i-1], A[i] + max(prevDiff, profit [t-1][i-1] – A[i-1]) 
# where prevDiff is max(profit[t-1][j] – A[j]) for all j in range [0, i-2]
def maxProfitOptimized(A, n, k):
    # code here
    profit = [[0 for i in range(n + 1)] for j in range(k + 1)]
                
    # Fill the table in bottom-up fashion
    for i in range(1, k + 1):
        prevDiff = float('-inf')
            
        for j in range(1, n):
            prevDiff = max(prevDiff, profit[i - 1][j - 1] -A[j - 1])
            profit[i][j] = max(profit[i][j - 1], A[j] + prevDiff)
    
    return profit[k][n-1]

As = [12, 14, 17, 10, 14, 13, 12, 15]
k = 3
maxProfitOptimized(As, len(As), k)