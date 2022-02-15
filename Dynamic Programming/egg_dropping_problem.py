def eggDrop(n, k):
        # code here
        eggFloor = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            eggFloor[i][1] = 1
            eggFloor[i][0] = 0
            
        for j in range(1, k+1):
            eggFloor[1][j] = j
            
        for i in range(2, n+1):
            for j in range(2, k+1):
                eggFloor[i][j] = float('inf')
                for x in range(1, j+1):
                    eggFloor[i][j] = min(eggFloor[i][j], 
                        1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]))
        return eggFloor[n][k]