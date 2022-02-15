
def fourSum(A, k):
    # code here
    # code here
    n = len(A)
    A.sort()
    quadruple = []
    for i in range(n-3):
        if i > 0 and A[i] == A[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and A[j] == A[j-1]:
                continue
            l = j + 1
            r = n - 1
            
            # To find the remaining two elements,  
            # move the index variables (l & r) 
            # toward each other. 
            while (l < r):
                old_l = l
                old_r = r
                if(A[i] + A[j] + A[l] + A[r] == k): 
                    quadruple.append([A[i], A[j], A[l], A[r]])
                    while l < r and A[l] == A[old_l]:
                        l += 1
                    while l < r and A[r] == A[old_r]:
                        r -= 1
                  
                elif (A[i] + A[j] + A[l] + A[r] < k): 
                    l += 1
                else: # A[i] + A[j] + A[l] + A[r] > X 
                    r -= 1
    return quadruple