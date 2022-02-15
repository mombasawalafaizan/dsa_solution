def isPowerofTwo(n):
    set_bits = 0
    while n > 0:
        n = n & (n-1)
        set_bits += 1
    return (set_bits == 1)