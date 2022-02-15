def isFeasible(mid, arr, n, k):
    elmts = 1
    pos = arr[0]
    for i in range(1, n):
        if (arr[i] - pos) >= mid:
            elmts += 1
            pos = arr[i]
            if elmts==k:
                return True
    return False


def minimumdistance(arr, n, k):
    arr.sort()
    res = -1
    low = 0
    high = arr[n-1] - arr[0] + 1
    while low<high:
        mid = (low+high)//2
        if isFeasible(mid, arr, n, k):
            res = max(res, mid)
            low = mid + 1
        else:
            high = mid
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = []
        for i in range(n):
            arr.append(int(input()))
        print(minimumdistance(arr, n, k))