def minimumCostforCutting(V, H, m, n):
    res = 0
    V.sort(reverse = True)
    H.sort(reverse = True)
    hzntl, vrtcl = 1, 1
    i, j = 0, 0

    while i < m and j < n:
        if V[i] > H[j]:
            res += (V[i]*vrtcl)
            hzntl += 1
            i += 1
        else:
            res += (H[j]*hzntl)
            vrtcl += 1
            j += 1

    remaining = 0
    while i < m:
        remaining += V[i]
        i += 1
    res += (remaining * vrtcl)

    remaining = 0
    while j < n:
        remaining += H[j]
        j += 1
    res += (remaining * hzntl)

    return res

if __name__ == '__main__':
    # m = 6
    # n = 4
    # X = [2, 1, 3, 1, 4]
    # Y = [4, 1, 2]
    # print(minimumCostforCutting(X, Y, m-1, n-1))
    t = int(input())
    for _ in range(t):
        blank = input()
        m, n = map(int, input().split())
        X, Y = [], []
        for i in range(m-1):
            X.append(int(input()))
        for i in range(n-1):
            Y.append(int(input()))
        print(minimumCostforCutting(X, Y, m-1, n-1))