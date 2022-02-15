from collections import deque
from typing import List

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        isInside = lambda x, y: 0<=x<len(image) and 0<=y<len(image[0])
        dx = (1, -1, 0, 0)
        dy = (0, 0, 1, -1)
        q = deque()
        q.append(Cell(sr, sc))
        color = image[sr][sc]
        while q:
            cell = q.popleft()
            image[cell.x][cell.y] = newColor
            for i in range(4):
                if isInside(cell.x + dx[i], cell.y + dy[i]) \
                    and image[cell.x + dx[i]][cell.y + dy[i]]==color:
                    q.append(Cell(cell.x + dx[i], cell.y + dy[i]))
        return image