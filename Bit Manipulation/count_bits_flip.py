def countBitsFlip(a,b):
    count = 0
    while a > 0 or b > 0:
        if a&1 != b&1:
            count += 1
        a >>= 1
        b >>= 1
    return count