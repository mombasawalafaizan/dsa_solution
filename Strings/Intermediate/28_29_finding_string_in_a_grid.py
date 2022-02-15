class FindWord:
    def __init__(self, diagonal: bool):
        self.diagonal = diagonal
        self.directions = [[0, 1], [1, 0], [-1, 0], [0, -1]] # Up, Right, Left, Down
        if self.diagonal:
            self.directions.extend([[-1, -1], [1, -1], [1, 1], [-1, 1]])

    def search_occurrence(self, word: str, grid: list, r: int, c: int, just_finding = False) -> int:
        '''Find if the word occurs 1 or more times from the starting point'''
        occur = 0 
        # Traverse in all directions
        for r_add, c_add in self.directions:
            i = 0
            # Starting points for each traversal
            cur_r = r  
            cur_c = c
            while i<len(word):
                if (not (0<=cur_r<len(grid) and 0<=cur_c<len(grid[0]))) or grid[cur_r][cur_c]!=word[i]:
                    break
                i+=1
                cur_r+=r_add
                cur_c+=c_add

            if i==len(word):
                # If the main goal is to find the position not occurrence
                if just_finding: 
                    return True
                occur += 1

        return occur

    def search(self, word: str, grid: list, r: int, c: int) -> bool:
        '''Finds if the word starts from [r][c] index in grid'''
        return bool(self.search_occurrence(word, grid, r, c, True))
        

def findingStringInGrid(grid: list, word: str, row: str, col: str):
    '''Find the word occurs in a given grid at which positions'''
    g = FindWord(True)
    flag = False
    for i in range(r):
        for j in range(c):
            if g.search(word, grid, i, j):
                flag=True
                print(str(i)+" "+str(j)+", ",end='')
    if flag:
        print()
    else:
        print(-1)   # If it does not occur
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        temp = input().split()
        arr = [temp[i:i+c] for i in range(0, r*c, c)]
        word = input()
        findingStringInGrid(arr, word, r, c)
        

# Recursive approach for searching in all directions
def internalSearch(ii, needle, r, c, hay, row_max, col_max):
    found = 0
    if r>=0 and r<=row_max and c <= col_max and c>=0 and needle[ii]==hay[r][c]:
        ii += 1
        if ii == len(needle):
            return 1
        found += internalSearch(ii, needle, r, c+1, hay, row_max, col_max)
        found += internalSearch(ii, needle, r, c-1, hay, row_max, col_max)
        found += internalSearch(ii, needle, r+1, c, hay, row_max, col_max)
        found += internalSearch(ii, needle, r-1, c, hay, row_max, col_max)
    return found