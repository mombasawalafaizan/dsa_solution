# The first few Catalan numbers for N = 0, 1, 2, 3, … are 
# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
# Catalan numbers satisfy the following recursive formula. 
# C(0) = 1 and C(n+1) = sum(C(i)C(n-i)) for  0 <= i <= n, for n >= 0

# DP solution 
def catalan(n):
    if (n == 0 or n == 1):
        return 1

    # Table to store results of subproblems
    catalan =[0]*(n+1)

    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j]* catalan[i-j-1]

    # Return last entry
    return catalan[n]


# Time complexity: O(N) Space complexity: O(1)
# For nth Catalan number formula is : (2nCn) / (n+1)
def binomialCoefficient(n, k):

    # since C(n, k) = C(n, n - k)
    if (k > n - k):
        k = n - k
    
    # initialize result
    res = 1
    
    # Calculate value of [n * (n-1) *---* (n-k + 1)]
    # / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
    
def findCatalan(n):
    #return the nth Catalan number.
    c = binomialCoefficient(2*n, n)
    return c//(n + 1)