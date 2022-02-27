import sys


def greaterThanM(arr, x, n):
    l = 0
    h = n - 1
    res = -1
    while l <= h:
        mid = (l + h) // 2
        if x >= arr[mid]:
            res = mid
            l = mid + 1
        else:
            h = mid - 1
    return res


if __name__ == "__main__":
    s = sys.stdin.read()
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    preSum = [0] * n
    preSum[0] = arr[0]
    for i in range(1, n):
        preSum[i] = arr[i] + preSum[i - 1]

    q = int(input())
    for _ in range(q):
        p = int(input())
        idx = greaterThanM(arr, p, n)
        if p < arr[0]:
            print(0, 0)
        else:
            print(idx + 1, preSum[idx])
