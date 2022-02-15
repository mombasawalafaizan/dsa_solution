class Solution(object):
    def feasible(self, num, cell, rows, cols, grid):
        r = cell // 9
        c = cell % 9
        g = 3 * (r // 3) + c // 3
        return num not in rows[r] and num not in cols[c] and num not in grid[g]

    def solve(self, board, idx, rows, cols, grid):
        if idx == 81:
            return True
        if board[idx//9][idx % 9] != '.':
            return self.solve(board, idx + 1, rows, cols, grid)
        for i in range(1, 10):
            if self.feasible(str(i), idx, rows, cols, grid):
                r, c = idx // 9, idx % 9
                g = 3 * (r // 3) + c // 3
                board[r][c] = str(i)
                rows[r].add(str(i))
                cols[c].add(str(i))
                grid[g].add(str(i))
                if self.solve(board, idx + 1, rows, cols, grid):
                    return True
                board[r][c] = '.'
                rows[r].remove(str(i))
                cols[c].remove(str(i))
                grid[g].remove(str(i))
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grid[3*(i//3)+j//3].add(board[i][j])

        self.solve(board, 0, rows, cols, grid)
