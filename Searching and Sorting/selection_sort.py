#Selection sort program
import time
import random

n = int(input("Enter how number to sort: "))
arr = random.sample(range(1, 100000), n)
start_time = time.time()

for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Time taken: ",str(time.time() - start_time))

