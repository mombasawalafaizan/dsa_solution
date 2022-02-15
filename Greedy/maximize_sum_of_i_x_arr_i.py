def Maximize(a, n): 
    # Complete the function
    a.sort()
    sum = 0
    for i in range(n):
        sum = (sum+i*a[i])%(10**9+7)
    return sum