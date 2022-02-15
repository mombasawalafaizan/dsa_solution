import random
def rearrangeAlternate(arr, n):
    i = 0
    j = 0
    reverse = False
    while j < n and i>=0:
        if arr[i] < 0:
            if not reverse:
                i = i + 2
                if i >= n:
                    reverse = True
                    if i == n:
                        i = n-1
                    else:
                        i = n-2
            else:
                i = i - 2
        else:
            if (reverse==False and (i<j or (i>j and j%2!=0)) and arr[j] < 0):
                arr[i], arr[j] = arr[j], arr[i]
            if reverse:
                if j >= i:
                    break
                elif j%2!=0 and arr[j]<0:
                    arr[i], arr[j] = arr[j], arr[i]
            j += 1

n = 10
arr = [random.randint(10, 50) for i in range(n)]
# arr = [48, 42, 2, 33, -8, -36, 29, -27, -13, 30]
print(arr)
rearrangeAlternate(arr, n)
print(arr)