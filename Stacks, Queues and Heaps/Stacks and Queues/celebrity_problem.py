def celebrity(M, n):
        # code here
        a = 0
        b = n-1
        while a < b:
            if M[a][b]:
                a+=1
            else:
                b-=1
                
        for i in range(n):
            if i!=a and (M[a][i]==1 or M[i][a]==0):
                return -1
        return a