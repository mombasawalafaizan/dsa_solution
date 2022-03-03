#Insertion sort program
import time
import random

n = int(input("Enter how number to sort: "))
arr = random.sample(range(1, 100000), n)
start_time = time.time()

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Time taken: ",str(time.time() - start_time))

