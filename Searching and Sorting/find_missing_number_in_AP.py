def findMissingInAP(arr):
    n = len(arr)
    if n <= 2:
        return float('inf')
    d = (arr[n-1] - arr[0])//n
    l = 0
    h = n-1
    while l <= h:
        mid = (l+h)//2
        if (arr[mid+1] - arr[mid]) != d:
            return arr[mid] + d
        if mid!=0 and (arr[mid] - arr[mid-1]) != d:
            return arr[mid-1] + d
        if arr[mid] == arr[0] + mid*d:
            l = mid + 1
        else:
            h = mid - 1
    return float('inf')
        