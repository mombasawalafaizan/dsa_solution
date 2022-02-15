def findMaxGold(mat, r, c):
    # If we dont want to change the matrix, use a list of size r and initialize it
    # with the values of last column and then update it max_values
    
    for j in range(c-2, -1, -1):
        for i in range(r):
            up = mat[i-1][j+1] if i-1 > 0 else 0 
            down = mat[i+1][j+1] if i+1 < r else 0
            right = mat[i][j+1]
            mat[i][j] += max(up, down, right)
    max_gold = -1
    for i in range(r):
        if mat[i][0] > max_gold:
            max_gold = mat[i][0]
    return max_gold

mat = [ [1, 3, 1, 5],
                   [2, 2, 4, 1],
                   [5, 0, 2, 3],
                   [0, 6, 1, 2]]

print(findMaxGold(mat, len(mat), len(mat[0])))