# Bubble sort program
import random


def bubbleSort(arr, n):
    last = n - 1
    for _ in range(n):
        swap_in_cur_pass = False
        for j in range(last):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_in_cur_pass = True
        if not swap_in_cur_pass:
            break
        last -= 1


if __name__ == "__main__":
    n = int(input("Enter how number to sort: "))
    arr = [random.randint(1, 20) for _ in range(n)]
    print("Before sorting : ", arr)
    bubbleSort(arr, n)
    print("After sorting  : ", arr)
