if __name__ == '__main__':
    t = int(input())
    for z in range(t):
        n, k, b, t = map(int, input().split())
        x = list(map(int, input().split()))
        v = list(map(int, input().split()))
        swaps = 0
        reachable = 0
        cantReach = 0
        
        for i in range(n-1, -1, -1):
            distance = b - x[i]
            canCover = t*v[i]
        
            if canCover >= distance:
                reachable += 1
                if cantReach > 0:
                    swaps += cantReach
            else:
                cantReach += 1
            if reachable == k:
                break

        if reachable < k:
            print('Case #'+str(z+1)+": IMPOSSIBLE")
        else:
            print('Case #'+str(z+1)+":",str(swaps))