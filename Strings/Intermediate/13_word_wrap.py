'''To understand the concept go to:
https://www.geeksforgeeks.org/word-wrap-problem-dp-19/
Solved using dynamic programming'''

def getSolution(p, n, sol):
    k = 0
    if p[n]==1:
        k=1
    else:
        k=getSolution(p , p[n]-1, sol)+1
    sol.extend([p[n], n])
    return k

def solveWordWrap(l, n, M):
    extras = [[0]*(n+1) for i in range(n+1)]
    lc = [[0]*(n+1) for i in range(n+1)]
    c = [0]*(n+1)
    p = [0]*(n+1)
    INF = float('inf')
    for i in range(1, n+1):
        extras[i][i]=M-l[i-1]
        for j in range(i+1, n+1):
            extras[i][j]= extras[i][j-1] - l[j-1]-1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if extras[i][j] < 0:
                lc[i][j] = float('inf')
            elif j==n and extras[i][j]>=0:
                lc[i][j] = 0
            else:
                lc[i][j] = extras[i][j]**2

    c[0]=0
    for j in range(1, n+1):
        c[j] = INF
        for i in range(1, j+1):
            if c[i-1]!=INF and lc[i][j]!=INF and (c[i-1]+lc[i][j]<c[j]):
                c[j] = c[i-1]+lc[i][j]
                p[j]=i
    sol = []
    getSolution(p, n, sol)
    for i in sol:
        print(i, end=' ')
    print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        M = int(input())
        solveWordWrap(l, n, M) 