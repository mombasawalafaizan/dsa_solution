# Given an integer N denoting the Length of a line segment. You need to cut the line segment in 
# such a way that the cut length of a line segment each time is either x , y or z. Here x, y, and z
# are integers.
# After performing all the cut operations, your total number of cut segments must be maximum.

# Input:
# N = 5
# x = 5, y = 3, z = 2
# Output: 2
# Explanation: Here total length is 5, and
# the cut lengths are 5, 3 and 2. We can
# make two segments of lengths 3 and 2.

def maximizeTheCuts(n,x,y,z):
    #returns: max number cuts.
    dp = [0] * (n+1)
    coins = (x, y, z)
    for i in range(3):
        for j in range(coins[i], n+1):
            if j == coins[i]:
                dp[j] = max(1, dp[j])
            elif (dp[j-coins[i]])!=0:
                dp[j] = max(dp[j], 1+dp[j-coins[i]])
    return dp[n]