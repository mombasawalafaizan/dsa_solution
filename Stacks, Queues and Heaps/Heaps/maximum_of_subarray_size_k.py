
def heapify(arr, i, n):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)

def search(arr, el):
    for i in range(len(arr)):
        if arr[i] == el:
            return i
    return -1

def findMaximum(arr, k):
    n = len(arr)
    if k >= n:
        return [max(arr)]
    j = k-1
    i = 0
    heap = arr[i:j+1]
    for i in range(k//2 - 1, -1, -1):
        heapify(heap, i, k)
    print(heap[0], end=' ')
    last = arr[i]
    i += 1
    j += 1
    nexts = arr[j]
    while j < n:
        heap[search(heap, last)] = nexts
        for i in range(k//2 - 1, -1, -1):
            heapify(heap, i, k)
        print(heap[0], end=' ')
        last = arr[i]
        j += 1
        i += 1 
        if j < n:
            nexts = arr[j]
    print()

if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    findMaximum(arr, k)