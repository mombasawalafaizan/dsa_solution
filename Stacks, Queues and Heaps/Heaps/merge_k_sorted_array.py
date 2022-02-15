def minHeapify(numbers, arr, i, k):
    s = i
    l = 2*i+1
    r = 2*i+2
    if l < k and numbers[(arr[s]-arr[s]%k)//k][arr[s]%k] > numbers[(arr[l]-arr[l]%k)//k][arr[l]%k]:
        s = l
    if r < k and numbers[(arr[s]-arr[s]%k)//k][arr[s]%k] > numbers[(arr[r]-arr[r]%k)//k][arr[r]%k]:
        s = r
    if s != i:
        arr[i], arr[s] = arr[s], arr[i]
        minHeapify(numbers, arr, s, k)
    
def popAndReplace(numbers, heap, k):
    cur_smallest = heap[0]
    if (cur_smallest+1)%k != 0:
        heap[0] = heap[0] + 1
    minHeapify(numbers, heap, 0, k)
    return cur_smallest
    
def merge(numbers):
    k = len(numbers)
    heap = [k*i for i in range(k)]
    for i in range(k//2-1, -1, -1):
        minHeapify(numbers, heap, i, k)
    ans = [0] * (k**2)
    for i in range(k*k):
        idx = popAndReplace(numbers, heap, k)
        ans[i] = numbers[(idx-idx%k)//k][idx%k]
        if (idx+1)%k==0:
            numbers[(idx-idx%k)//k][idx%k] = float('inf')
            minHeapify(numbers, heap, 0, k)
    return ans