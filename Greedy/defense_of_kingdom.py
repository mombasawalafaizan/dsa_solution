# Find the number of cells in the largest undefended rectangle.
# For each query of given row and col, they are occupied

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        c, r, q = map(int, input().split())
        cols = [0 for _ in range(q+2)]
        rows = [0 for _ in range(q+2)]
        for i in range(q):
            cur_c, cur_r = map(int, input().split())
            cols[i] = cur_c
            rows[i] = cur_r
        cols[q] = c + 1
        rows[q] = r + 1
        cols.sort()
        rows.sort()
        max_width = 0
        max_height = 0
        
        for i in range(1, q+1):
            temp_x = cols[i] - cols[i-1]
            temp_y = rows[i] - rows[i-1]
            if max_width < temp_x:
                max_width = temp_x
            if max_height < temp_y:
                max_height = temp_y
        print((max_height-1)*(max_width-1))
            