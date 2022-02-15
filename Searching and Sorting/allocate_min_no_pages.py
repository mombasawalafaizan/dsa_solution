def isFeasible(arr, n, m, cur_min):
    parts = 1
    cur_sum = 0
    for i in range(n):
        if arr[i] > cur_min:
            return False
        if (cur_sum + arr[i]) <= cur_min:
            cur_sum += arr[i]
        else:
            cur_sum = arr[i]
            parts += 1
            if parts > m:
                return False
    return True
    
def findPages(arr, n, m):
    # n: no of book
    # m: no of students
    
    #return: the expected answer if possible else return -1
    if m > n:
        return -1
    res = float('inf')
    left = arr[0]
    right = sum(arr)
    while left <= right:
        mid = (left+right)//2
        if isFeasible(arr, n, m, mid):
            res = min(res, mid)
            right = mid - 1
        else:
            left = mid + 1
    return res