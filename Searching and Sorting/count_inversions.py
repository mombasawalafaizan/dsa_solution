import random


def mergeSort(arr, n):
    temp = [0] * n
    return _mergeSort(arr, temp, 0, n - 1)


def _mergeSort(arr, temp, l, h):
    inv_cnt = 0
    if l < h:
        mid = (l + h) // 2
        inv_cnt += _mergeSort(arr, temp, l, mid)
        inv_cnt += _mergeSort(arr, temp, mid + 1, h)
        inv_cnt += merge(arr, temp, l, mid, h)
    return inv_cnt


def merge(arr, temp, left, mid, right):
    i = left
    k = left
    j = mid + 1
    inv_cnt = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            # arr[i], arr[i+1], ... arr[mid] are greater than arr[j], hence increase the count
            inv_cnt += mid + 1 - i
            temp[k] = arr[j]
            j += 1
            k += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for var in range(left, right + 1):
        arr[var] = temp[var]
    return inv_cnt


n = 10
arr = [random.randint(1, 100) for i in range(n)]
arr.sort(reverse=True)
print(arr)
print(mergeSort(arr, n))
print("Sorted: ", arr)
