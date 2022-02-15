import random
class FreqCount:
    def __init__(self):
        self.data = 0
        self.count = 0

def moreThanNdK(arr, n, k):
    if k < 2:
        return []
    temp = [FreqCount() for i in range(k-1)]
    for i in range(n):
        j = 0
        while j < k-1:
            if temp[j].data == arr[i]:
                temp[j].count += 1
                break
            j += 1
        if j == k-1:
            l = 0
            while l < k-1:
                if temp[l].count == 0:
                    temp[l].data = arr[i]
                    temp[l].count = 1
                    break
                l += 1
            if l == k-1:
                for m in range(k-1):
                    temp[m].count -= 1

    res = []
    for i in range(k-1):
        actual_count = 0
        for j in range(n):
            if arr[j] == temp[i].data:
                actual_count += 1
        if actual_count > n//k:
            res.append(temp[i].data)
    return res

n = 8
arr = [random.randint(1, 3) for i in range(n)]
k = 3
print(arr)
print(moreThanNdK(arr, n, k))