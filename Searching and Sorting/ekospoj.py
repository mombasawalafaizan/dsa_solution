def eko(arr, n, k):
    low = 0
    high = max(arr)
    count, h, mid = 0, 0, 0
    while low <= high:
        mid = (high+low)//2
        count = 0
        for i in range(n):
            count += (arr[i]-mid) if (arr[i]-mid)>0 else 0
        if count == k:
            h = mid
            break
        elif count < k:
            high = mid - 1
        else:
            low = mid + 1
            if mid > h:
                h = mid
    return h

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(eko(arr, n, k))