from collections import deque


def BFS(i, j, grid, id):
    r = len(grid)
    c = len(grid[0])
    cur_area = 0
    queue = deque()
    queue.append((i, j))
    grid[i][j] = id
    while queue:
        pos = queue.popleft()
        cur_area += 1
        if pos[0]+1 < r and grid[pos[0]+1][pos[1]] == 1:
            queue.append((pos[0]+1, pos[1]))
            grid[pos[0]+1][pos[1]] = id
        if pos[0]-1 >= 0 and grid[pos[0]-1][pos[1]] == 1:
            queue.append((pos[0]-1, pos[1]))
            grid[pos[0]-1][pos[1]] = id
        if pos[1]-1 >= 0 and grid[pos[0]][pos[1]-1] == 1:
            queue.append((pos[0], pos[1]-1))
            grid[pos[0]][pos[1]-1] = id
        if pos[1]+1 < c and grid[pos[0]][pos[1]+1] == 1:
            queue.append((pos[0], pos[1]+1))
            grid[pos[0]][pos[1]+1] = id
    return cur_area


def largestIsland(grid):
    r = len(grid)
    c = len(grid[0])
    islands_area = [0, 0]
    id = 2
    max_area = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                cur_area = BFS(i, j, grid, id)
                max_area = max(cur_area, max_area)
                islands_area.append(cur_area)
                id += 1

    if id == 2:
        return 1
    elif id == 3 and max_area == r*c:
        return max_area

    def check(i, j):
        return (0 <= i < r and 0 <= j < c and grid[i][j] != 0)
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    print(islands_area, grid)
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                different_id = set()
                for k in range(4):
                    if check(i+dir[k][0], j+dir[k][1]):
                        different_id.add(grid[i+dir[k][0]][j+dir[k][1]])
                cur_area = 1
                for id in different_id:
                    cur_area += islands_area[id]
                max_area = max(max_area, cur_area)

    return max_area


mat = [[1, 0, 1, 1, 0],
       [1, 0, 1, 0, 1],
       [0, 0, 1, 1, 1],
       [1, 1, 0, 0, 0]]
mat = [[1, 1], [1, 1]]
mat = [[0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 0, 0],
       [0, 1, 0, 0, 1, 0, 0],
       [1, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 0, 0],
       [0, 1, 1, 1, 1, 0, 0]]
mat = [[1, 0, 0, 1, 1],
       [1, 0, 0, 1, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 0, 1],
       [0, 0, 0, 1, 0]]
print(largestIsland(mat))
