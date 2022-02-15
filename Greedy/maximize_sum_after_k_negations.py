from heapq import heapify, heapreplace

def maximizeSum(arr, n, k):
    heapify(arr)
    for i in range(k):
        temp = (-1) * arr[0]
        heapreplace(arr, temp)
    return sum(arr)

def maximizeSum(arr, n, k):
    # Your code goes here
    arr.sort()
 
    Sum = 0
    i = 0
    minimum = float('inf')
 
    while (i < n and k > 0):
 
        # If we find a 0 in our
        # sorted array, we stop
        if (arr[i] >= 0):
            minimum = min(minimum, arr[i])
            break
        else:
            arr[i] = (-1) * arr[i]
            minimum = arr[i]
            Sum += arr[i]
            k = k - 1
 
        i += 1
 
    # Calculating sum
    for j in range(i, n):
        Sum += arr[j]
    if k!=0 and k%2!=0:
        Sum -= 2*minimum
    
    return Sum