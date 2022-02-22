# User function Template for python3
def calculatePossibilities(grid, r, c):
    start_row = 3 * (r // 3)
    start_col = 3 * (c // 3)
    subgrid_possib, cur_row_possib, cur_col_possib = 0, 0, 0
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] != 0:
                subgrid_possib = subgrid_possib | (1 << (grid[i][j] - 1))
    for i in range(9):
        if grid[r][i] > 0:
            cur_row_possib = cur_row_possib | (1 << (grid[r][i] - 1))
        if grid[i][c] > 0:
            cur_col_possib = cur_col_possib | (1 << (grid[i][c] - 1))
    return (
        (~subgrid_possib & (2 ** 9 - 1))
        & (~cur_row_possib & (2 ** 9 - 1))
        & (~cur_col_possib & (2 ** 9 - 1))
    )


def solveUtil(grid, idx, empty):
    j = idx % 9
    i = idx // 9
    if idx == 81:
        return False
    if grid[i][j] != 0:
        if solveUtil(grid, idx + 1, empty):
            return True
    else:
        possib = calculatePossibilities(grid, i, j)
        cur_possib = 1
        while possib > 0:
            if possib % 2 != 0:
                grid[i][j] = cur_possib
                if empty == 1:
                    return True
                if solveUtil(grid, idx + 1, empty - 1):
                    return True
                grid[i][j] = 0
            possib = possib >> 1
            cur_possib += 1
    return False


def solve_sudoku(grid):
    empty = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty += 1
    # Full sudoku
    if empty == 0:
        return True
    return solveUtil(grid, 0, empty)


def print_grid(arr):

    # Your code here
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
    print()
