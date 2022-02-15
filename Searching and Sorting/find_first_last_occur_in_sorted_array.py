def findFirstOccur(arr, l, r, n, x):
    if l <= r:
        mid = (l+r)//2
        if arr[mid] == x:
            if mid!=0 and arr[mid-1] == arr[mid]:
                return findFirstOccur(arr, l, mid, n, x)
            else:
                return mid
        if arr[mid] > x:
            return findFirstOccur(arr, l, mid, n, x)
        return findFirstOccur(arr, mid+1, r, n, x)
    return -1
    
def findLastOccur(arr, l, r, n, x):
    if l <= r:
        mid = (l+r)//2
        if arr[mid] == x:
            if mid!=n-1 and arr[mid+1] == arr[mid]:
                return findLastOccur(arr, mid+1, r, n, x)
            else:
                return mid
        if arr[mid] > x:
            return findLastOccur(arr, l, mid, n, x)
        return findLastOccur(arr, mid+1, r, n, x)
    return -1
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        first = findFirstOccur(arr, 0, n-1, n, x)
        if first == -1:
            print(-1)
        else:
            last = findLastOccur(arr, 0, n-1, n, x)
            print(first, last)