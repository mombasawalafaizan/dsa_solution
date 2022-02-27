import random


def simpleMergeUtil(arr, l, mid, h):
    if arr[mid] <= arr[mid + 1]:
        return
    i = l
    j = mid + 1
    idx = 0
    temp = arr[l : h + 1]
    while i <= mid and j <= h:
        if arr[i] < arr[j]:
            temp[idx] = arr[i]
            idx += 1
            i += 1
        else:
            temp[idx] = arr[j]
            idx += 1
            j += 1
    while i <= mid:
        temp[idx] = arr[i]
        idx += 1
        i += 1
    while j <= h:
        temp[idx] = arr[j]
        idx += 1
        j += 1
    for i in range(l, h + 1):
        arr[i] = temp[i - l]


def inplaceMergeUtil(arr, l, mid, h):
    if arr[mid] <= arr[mid + 1]:
        return
    i = l
    j = mid + 1
    while i < j and j <= h:
        if arr[i] <= arr[j]:
            i += 1
        else:
            temp = arr[j]
            for k in range(j, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = temp
            i += 1
            j += 1


def mergeSort(arr, l, h):
    if l < h:
        mid = (l + h) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, h)
        simpleMergeUtil(arr, l, mid, h)


def inplaceMergeSort(arr, l, h):
    if l < h:
        mid = (l + h) // 2
        inplaceMergeSort(arr, l, mid)
        inplaceMergeSort(arr, mid + 1, h)
        inplaceMergeUtil(arr, l, mid, h)


def isSorted(arr):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    for _ in range(10):
        n = random.randint(1, 100)
        arr = [random.randint(1, 90) for _ in range(n)]
        mergeSort(arr, 0, len(arr) - 1)
        if not isSorted(arr):
            print("Not sorted", arr)
