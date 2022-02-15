if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        k = 0
        while k < n and arr[k] == 1:
            print('1', end= ' ')
            k += 1
        if k==n-2 and arr[k]==2:
            print('2 3')
            continue
        for i in range(n-1, k-1, -1):
            print(arr[i], end=' ')
        print()