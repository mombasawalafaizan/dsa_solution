import random
def maxHeapify(arr, i, n):
    l = 2*i + 1
    r = 2*i + 2
    temp = i
    if l < n and arr[temp] < arr[l]:
        temp = l
    if r < n and arr[temp] < arr[r]:
        temp = r
    if temp!=i:
        arr[temp], arr[i] = arr[i], arr[temp]
        maxHeapify(arr, temp, n)

def minHeapify(arr, i, n):
    l = 2*i + 1
    r = 2*i + 2
    temp = i
    if l < n and arr[temp] > arr[l]:
        temp = l
    if r < n and arr[temp] > arr[r]:
        temp = r
    if temp!=i:
        arr[temp], arr[i] = arr[i], arr[temp]
        minHeapify(arr, temp, n)

if __name__ == "__main__":
    n = 11
    arr = [random.randint(1, 100) for i in range(n)]
    print(arr)
    for i in range(n//2 - 1,-1, -1):
        maxHeapify(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, 0, i) 
    print(arr)    