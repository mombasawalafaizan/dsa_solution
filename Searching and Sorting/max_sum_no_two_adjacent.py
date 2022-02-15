def maxLoot(arr, idx):
    if idx<0:
        return 0
    return max(arr[idx] + maxLoot(arr, idx-2), maxLoot(arr, idx-1))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxLoot(arr, n-1))