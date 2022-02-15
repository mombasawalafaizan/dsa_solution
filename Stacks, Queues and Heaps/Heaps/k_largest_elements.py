from heapq import _heapify_max, _heappop_max

def maxHeapify(arr, i, n):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[largest] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest!=i:
            arr[largest], arr[i] = arr[i], arr[largest]
            maxHeapify(arr, largest, n)
            
def kLargest(arr, n, k):
    for i in range(n//2-1, -1, -1):
        maxHeapify(arr, i, n)
    ans = []
    for i in range(n-1, n-k-1, -1):
        ans.append(arr[0])
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, 0, i)
    return ans

    # _heapify_max(arr)
    # ans = []
    # for i in range(k):
    #     ans.append(_heappop_max(arr))
    # return ans