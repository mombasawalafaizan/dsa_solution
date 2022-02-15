def findPosition(self, n):
    last_pos = cur_pos = 1
    cnt = 0
    while n > 0:
        if n & 1:
            last_pos = cur_pos
            cnt += 1
        n = n >> 1
        cur_pos += 1
    return last_pos if cnt==1 else -1