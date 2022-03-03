import time
import random


def partition(arr, p, q):
    """Find the partition such that elements on left are smaller and on right
    are greater"""
    i = p - 1
    pivot = arr[q]  # Taking last element as key or pivot
    # Find the place to insert the pivot
    for j in range(p, q):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[q], arr[i + 1] = arr[i + 1], arr[q]
    return i + 1


def quickSort(arr, p, q):
    if p < q:
        r = partition(arr, p, q)  # Find the pivot
        quickSort(arr, p, r - 1)  # Sort the left array from pivot
        quickSort(arr, r + 1, q)  # Sort the right array from pivot


n = int(input("Enter how number to sort: "))
arr = random.sample(range(1, 100000), n)
start_time = time.time()
quickSort(arr, 0, len(arr) - 1)
print("Time taken: ", str(time.time() - start_time))
print(arr)
