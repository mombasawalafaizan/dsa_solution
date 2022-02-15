def LCSof3(A,B,C,n1,n2,n3):
    # code here
    L = [[[0 for _ in range(n3+1)] for _ in range(n2+1)] 
        for _ in range(n1+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if A[i-1]==B[j-1] and A[i-1]==C[k-1]:
                    L[i][j][k] = 1 + L[i-1][j-1][k-1]
                else:
                    L[i][j][k] = max(max(L[i-1][j][k], L[i][j-1][k]), 
                        L[i][j][k-1])
    return L[n1][n2][n3]