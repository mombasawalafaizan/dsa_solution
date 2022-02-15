from collections import deque
 
 
# check if specified row and column are valid matrix index
def isValid(i, j):
    return (0 <= i < M) and (0 <= j < N)
 
 
# check if current cell is an open area and its
# distance from mine is not yet calculated
def isSafe(i, j, mat, result):
    return mat[i][j] == 'O' and result[i][j] == -1
 
 
# Replace all O's in the matrix with their shortest distance
# from the nearest mine
def updateDistance(mat, result):
 
    # initialize an empty queue
    q = deque()
 
    # find all mines location and add them to the queue
    for i in range(M):
        for j in range(N):
            # if current cell represents a mine
            if mat[i][j] == 'M':
                q.append((i, j, 0))
 
                # update mine distance as 0
                result[i][j] = 0
 
            # else initialize mine distance by as -1
            else:
                result[i][j] = -1
 
    # lists to get indices of 4 adjacent cells of a given cell
    R = [0, -1, 0, 1]
    C = [-1, 0, 1, 0]
 
    # do for each in the queue
    while q:
 
        # dequeue the front cell
        x, y, distance = q.popleft()
 
        # update the 4 adjacent cells of the front node in the queue
        for i in range(4):
            # enqueue the adjacent cell if it is valid, unvisited,
            # and has a path through it
            if isValid(x + R[i], y + C[i]) and isSafe(x + R[i], y + C[i], mat, result):
                result[x + R[i]][y + C[i]] = distance + 1
                q.append((x + R[i], y + C[i], distance + 1))
 
 
# Find shortest distance of every cell from land mine in a Maze
if __name__ == '__main__':
 
    mat = [
        ['O', 'M', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'O', 'M'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'O', 'M', 'O', 'O'],
        ['O', 'X', 'X', 'M', 'O']
    ]
 
    # M x N matrix
    M = 6
    N = 5
 
    result = [[0 for x in range(N)] for y in range(M)]
    updateDistance(mat, result)
 
    # print results
    for i in range(M):
        for h in range(N):
            print('{:2d}'.format(result[i][h]), end=' ')
        print()