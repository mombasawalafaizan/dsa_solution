def threeWayPartition(array, n, a, b):
    # Code here
    i = 0
    j = n-1
    k = 0
    arr = array[:]
    while k <= j:
        if arr[k]>b:
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
        elif arr[k]<a:
            arr[k], arr[i] = arr[i], arr[k]
            i += 1
            k += 1
        else:
            k+=1
    return arr