# This take O(no. of set bits in number) time
def setBits(N):
    cnt = 0
    while N > 0:
        N = N & (N-1)
        cnt += 1
    return cnt

# This take O(log2n) time
def setBits(N):
    cnt = 0
    while N > 0:
        cnt += N & 1
        N = N >> 1
    return cnt