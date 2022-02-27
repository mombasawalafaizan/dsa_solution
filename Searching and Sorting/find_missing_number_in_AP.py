def findMissingInAP(arr):
    n = len(arr)
    if n <= 2:
        return float("inf")
    d = (arr[n - 1] - arr[0]) // n
    l = 0
    h = n - 1
    while l < h:
        mid = (l + h) // 2
        if (arr[mid + 1] - arr[mid]) != d:
            return arr[mid] + d
        if arr[mid] == arr[0] + mid * d:
            l = mid + 1
        else:
            h = mid
    return float("inf")


print(findMissingInAP([2, 4, 8, 10, 12, 14]))
