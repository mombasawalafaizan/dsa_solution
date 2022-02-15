# This is done by Faizan
def copySetBitsInRange(x, y, l, r):
    if l<1 or r>32 or l>r:
        return 
    temp = 2**(r-l+1)-1
    temp <<= (l-1)
    return (temp & y) | x

def copySetBitsGFG(x, y, l, r):
    if l<1 or r>32 or l>r:
        return 
    masklen = (1<<(r-l+1))-1
    mask = ((masklen)<<(l-1)) & y
    return x | mask