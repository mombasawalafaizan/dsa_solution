def findPair(matrix, n):
    if n<=1:
        return float('inf')
    max_val = matrix[n-1][n-1]
    max_dif = max_val - matrix[n-2][n-2]
    for i in range(n-1, 0, -1):
        for j in range(n-1, 0, -1):
            if max_val < matrix[i][j]:
                max_val = matrix[i][j]
            if max_dif < (max_val - matrix[i-1][j-1]):
                max_dif = (max_val - matrix[i-1][j-1])
                print('a', i-1, 'b', j-1, 'val', matrix[i-1][j-1], 'max_val', max_val)
    return max_dif

matrix = [[ 1, 2, -1, -4, -20 ], 
       [-8, -3, 4, 2, 1 ], 
       [ 3, 8, 6, 1, 3 ], 
       [ -4, -1, 1, 7, -6] , 
       [0, -4, 10, -5, 1 ]]
print(findPair(matrix, 5))