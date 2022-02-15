def printList(arr, s):
    n = len(arr[0])
    q = list(s)
    for i in arr:
        print(i)
    
def countPS(s):
    n = len(s)
    cps = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n):
        cps[i][i] = 1
    for L in range(2, n+1):
        for i in range(n):
            k = L + i - 1
            # print(i, k)
            if k < n:
                if s[i]==s[k]:
                    cps[i][k] = cps[i][k-1] + cps[i+1][k] + 1
                else:
                    cps[i][k] = cps[i][k-1] + cps[i+1][k] - cps[i+1][k-1]
            # printList(cps, s)
    return cps[0][n-1]

print(countPS('aab  '))