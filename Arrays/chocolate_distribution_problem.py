def findMinDifference(arr, n, m):
    if m == n:
        return max(arr) - min(arr)
    if m==0:
        return 0
    arr.sort()
    min_dif = float('inf')
    for i in range(n-m+1):
        if min_dif > arr[i+m-1]-arr[i]:
            min_dif = arr[i+m-1] - arr[i]
    return min_dif
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        m = int(input())
        print(findMinDifference(arr, n, m))