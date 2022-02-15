# DP solution
# Space complexity: O(n) and Time complexity: O(n^2)
# This is similar to Longest Increasing Subsequence
def longestAltSubs(arr):
    max_val = 1
    n = len(arr)
    eq = [[1 for _ in range(n)] for _ in range(2)]
    
    # You can use this loop variables
    # for i in range(1, n):
    #     for j in range(0, i):
    # OR
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[j] < arr[i] and (eq[1][j]+1) > eq[0][i]:
                    eq[0][i] = eq[1][j] + 1
            if arr[j] > arr[i] and (eq[0][j]+1) > eq[1][i]:
                    eq[1][i] = eq[0][j] + 1
    max_val = max(eq[0], eq[1])
    return max_val


def LAS(arr, n):
   
    # "inc" and "dec" intialized as 1
    # as single element is still LAS
    inc = 1
    dec = 1
     
    # Iterate from second element
    for i in range(1,n):
       
        if (arr[i] > arr[i-1]):
           
            # "inc" changes iff "dec" 
            # changes
            inc = dec + 1
        elif (arr[i] < arr[i-1]):
           
            # "dec" changes iff "inc" 
            # changes
            dec = inc + 1
             
    # Return the maximum length
    return max(inc, dec)