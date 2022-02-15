from collections import deque
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        fni=0
        for i in range(k-1, n):
            while fni < i and (fni <= i-k or arr[fni] > 0):
                fni += 1
            fne = arr[fni] if arr[fni] < 0 else 0
            print(fne, end=' ')
        print()

        # queue = deque()
        # for i in range(n):
        #     if arr[i] < 0:
        #         queue.append(arr[i])
        #     if i>=k-1:
        #         if not queue:
        #             print('0', end=' ')
        #         else:
        #             print(queue[0], end=' ')
        #             if arr[i-k+1] == queue[0]:
        #                 queue.popleft()
        # print()