def findCommon(matrix, rows, cols):
    column = [cols-1] * rows
    common = []
    min_row = 0
    while column[min_row] >= 0:
        for i in range(rows):
            if matrix[i][column[i]] < matrix[min_row][column[min_row]]:
                min_row = i
        
        eq_count = 0
        for i in range(rows):
            if matrix[i][column[i]] > matrix[min_row][column[min_row]]:
                if column[i] == 0:
                    return common
                column[i] -= 1
            else:
                eq_count += 1
        
        if eq_count==rows:
            common.append(matrix[min_row][column[min_row]])
            for i in range(rows):
                column[i] -= 1
                if column[i] < 0:
                    return common

    return common

print(findCommon([[2, 3, 3, 3, 4, 5, 5, 5], [1, 3, 4, 4, 5, 6, 6, 6], [4, 4, 5, 5, 5, 6, 6, 7], [1, 4, 4, 5, 6, 7, 7, 7], [1, 1, 2, 3, 4, 5, 6, 7]],5,8))