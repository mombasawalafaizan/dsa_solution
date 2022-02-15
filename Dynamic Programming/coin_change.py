# Given a value N, if we want to make change for N cents, and we have infinite supply of each of
# S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
# The order of coins doesn’t matter.
# For example, for N = 4 and S = {1,2,3}, there are four solutions:
# {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
# For N = 10 and S = {2, 5, 3, 6}, there are five solutions:
# {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

# NOTE: This problem is not SAME as MAKE CHANGE problem. In this problem, we want to
# find the number of possible changes whereas in MAKE CHANGE, we have to identify the
# number of coins in the best possible change.

# Time Complexity: O(mn) and Space Complexity: O(mn)
from typing_extensions import IntVar


def count(S, m, n):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):

            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    print(0, S)
    for i in range(len(table)):
        print(i, table[i])
    return table[n][m - 1]


# Time Complexity: O(mn) and Space Complexity: O(n)
def county(S, m, n):

    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
    return table[n]


def makeChange(n: int, d: list, k: int):
    """
    n: value for which to make change
    d:array of coins
    k: number of available coins
    """

    # 2D DP formula = dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i]])
    # Here we are calculating column-wise so,
    C = [float("inf")] * (n + 1)  # The number of coins for change upto n
    C[0] = 0

    # Which coin is added for each change upto n (index are stored in this (starting index is considered 1))
    S = [0] * (n + 1)

    for i in range(k):
        for j in range(d[i], n + 1):
            # If we don't want coins to be considered remove the condition block
            if C[j] > (1 + C[j - d[i]]):
                S[j] = i + 1
            C[j] = min(C[j], 1 + C[j - d[i]])

    # If no solution is possible
    if C[n] == float("inf"):
        return []

    # Calculating which coins constitute the solution
    i = n
    j = C[n]
    coins = [0] * C[n]
    while i > 0:
        coins[j - 1] = d[S[i] - 1]
        j -= 1
        i -= d[S[i] - 1]
    return coins


S = [2, 4, 6]
# print(count(S, len(S), 8))
print(makeChange(8, S, len(S)))
