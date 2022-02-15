def findPair(arr, n, diff):
    arr.sort()
    i, j = 0, 1
    while i<n and j < n:
        if i!=j and (arr[j] - arr[i]) == diff:
            return 1
        elif (arr[j]-arr[i])>diff:
            i += 1
        else:
            j += 1
    return -1
    # Or use binary search with O(nlogn)
    # for i in range(n-1):
    #     idx = bsearch(arr, i+1, n-1,(diff+arr[i]))
    #     if idx!=-1 and i!=idx:
    #         return 1
    # return -1