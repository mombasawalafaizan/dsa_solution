import random
for m in range(15):
    n = 20
    arr = [random.randint(-100, 80) for i in range(n)]
    # This is where the algorithm starts
    i = 0
    j = n-1
    prev = arr[:]
    while i<=j:
        if arr[i] < 0:
            i += 1
        elif arr[j] >= 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    