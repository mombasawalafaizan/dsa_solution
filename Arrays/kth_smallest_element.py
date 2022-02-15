import random

def partition(arr, l, r):
    pivot = arr[r]
    i = l
    j = r-1
    for j in range(l, r):
        if pivot >= arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def randomPartition(arr, l, r):
    pivot = random.randint(l, r)
    arr[pivot], arr[r] = arr[r], arr[pivot]
    return partition(arr, l, r)

def kthSmallest(arr, l, r, k):
    if k>0 and k<=r-l+1:
        pos = randomPartition(arr, l, r)
        if pos == k-1:
            return arr[k]
        if pos > k-1:
            return kthSmallest(arr, l, pos-1, k)
        return kthSmallest(arr, pos+1, r, k-pos+l-1)

if __name__ == '__main__':
    n = 20
    arr = [random.randint(1, 1000) for i in range(n)]
    kthSmallest(arr, 0, n-1)
    print(arr)