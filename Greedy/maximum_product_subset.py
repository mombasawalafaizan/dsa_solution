def maxProductSubset(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    maxNegative = float('-inf')
    product = 1
    zeros = 0
    cnt_negtvs = 0
    for i in range(n):
        if arr[i] == 0:
            zeros += 1
            continue
        if arr[i] < 0:
            cnt_negtvs += 1
            maxNegative = max(maxNegative, arr[i])
        product = product * arr[i]
    
    if zeros == n:
        return 0
    
    if cnt_negtvs%2!=0:
        # Exceptional case: There is only 
        # negative and all other are zeros 
        if (cnt_negtvs == 1 and zeros > 0 and
            zeros + cnt_negtvs == n):
            return 0

        product = product // maxNegative
    return product
    