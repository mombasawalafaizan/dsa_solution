#User function Template for python3
from collections import deque
class cell:
    
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
        
# checks whether given position is 
# inside the board
def isInside(x, y, N):
    if (x >= 1 and x <= N and 
        y >= 1 and y <= N): 
        return True
    return False


def minStepToReachTarget(knightpos, targetpos, N):
    '''
    knightpos: (x,y) tuple of current position coordinate
    targetpos: (x,y) tuple of target position coordinate 
    N: size of board
    
    return: minimum steps the Knight will take to reach the target position
    '''
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    
    queue = deque()
    
    # push starting position of knight
    # with 0 distance
    queue.append(cell(knightpos[0], knightpos[1], 0))
    
    # make all cell unvisited 
    visited = [[False for i in range(N + 1)] 
                      for j in range(N + 1)]
    
    # visit starting state
    visited[knightpos[0]][knightpos[1]] = True
    
    # loop untill we have one element in queue 
    while(len(queue) > 0):
        
        t = queue[0]
        queue.popleft()
        
        # if current cell is equal to target 
        # cell, return its distance 
        if(t.x == targetpos[0] and 
           t.y == targetpos[1]):
            return t.dist
            
        # iterate for all reachable states 
        for i in range(8):
            
            x = t.x + dx[i]
            y = t.y + dy[i]
            
            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

print(minStepToReachTarget((2, 4), (3, 4), 4))