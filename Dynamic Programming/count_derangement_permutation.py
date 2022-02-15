# Python program to count derangements 
# Recurrence relation : countDer(n) = (n - 1) * [countDer(n - 1) + countDer(n - 2)]
def countDer(n):

    # Base Case
    if n == 1 or n == 2:
        return n-1

    # Variables for storing prevoius values
    a = 0
    b = 1

    # using above recursive formula 
    for i in range(3, n + 1): 
        cur = (i-1)*(a+b)
        a = b
        b = cur

    # Return result for n 
    return b 