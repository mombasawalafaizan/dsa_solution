import sys


def isSafe(i, j, r, c, m):
    return 0 <= i < r and 0 <= j < c and m[i][j] != 0


def SSRHelper(i, j, m, cur_dist, cur_min):
    r, c = len(m), len(m[0])
    # This array is defined such that first go left, then up down and lastly go right
    pos = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # We reached the end, and this surely is the current smallest distance
    if j == c - 1:
        return cur_dist

    # Optimization:
    # No need to go further if we cannot reach the last col even in a straight path
    # and reduce the minimum distance
    if (c - 1 - j) + cur_dist >= cur_min:
        return sys.maxsize

    prev_min = cur_min
    for x, y in pos:
        m[i][j] = 0
        if isSafe(i + x, j + y, r, c, m):
            res = SSRHelper(i + x, j + y, m, cur_dist + 1, prev_min)
            prev_min = min(prev_min, res)
        m[i][j] = 1  # Backtrack
    return prev_min


def shortestSafeRoute(matrix):
    # Modify the matrix, so that 0 indicates cell that cannot be travelled
    m = [row[:] for row in matrix]
    rows = len(m)
    cols = len(m[0])

    # Make the adjacent cells untraversable
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i > 0:
                    m[i - 1][j] = 0
                if i < rows - 1:
                    m[i + 1][j] = 0
                if j > 0:
                    m[i][j - 1] = 0
                if j < cols - 1:
                    m[i][j + 1] = 0

    min_travel = [sys.maxsize]
    for start_pos in range(rows):
        if m[start_pos][0] != 0:
            cur_res = SSRHelper(start_pos, 0, m, 0, min_travel[0])
            min_travel[0] = min(min_travel[0], cur_res)

            # Optimization: If the shortest possible distance is achieved, no need to check
            # for other routes
            if min_travel[0] == cols - 1:
                break

    return min_travel[0]


matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
]
print(shortestSafeRoute(matrix))
