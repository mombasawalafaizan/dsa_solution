from math import ceil, log2

def getSumUtil(st, ss, se, qs, qe, si):
    print('ss:', ss, 'se:', se, 'si:', si)
    if qs <= ss and qe >= se:
        print('condition 1')
        return st[si]
    
    if se < qs or ss > qe:
        print('condition 2')
        return 0

    mid = ss + (se-ss)//2
    return max(getSumUtil(st, ss, mid, qs, qe, 2*si+1),getSumUtil(st, mid+1, se, qs, qe, 2*si+2))

def getSum(st, n, qs, qe):
    if qs<0 or qe>n-1 or qs > qe:
        print('Invalid input')
        return -1
    return getSumUtil(st, 0, n-1, qs, qe, 0)

    
def constructSTUtil(arr, ss, se, st, si):
    # print('st in construct util: ', st)
    # print('ss:', ss, 'se:', se, 'si:', si)
    if ss==se:
        st[si] = arr[ss]
        return arr[ss]

    mid = ss + (se-ss)//2

    st[si] = max(constructSTUtil(arr, ss, mid, st, si*2+1) , constructSTUtil(arr, mid+1, se, st, si*2+2))
    return st[si]

def constructST(arr, n):
    x = (int)(ceil(log2(n)))
    max_size = 2 * (int)(2**x) -1 
    st = [0] * max_size
    constructSTUtil(arr, 0, n-1, st, 0)
    return st

if __name__ == "__main__":
    arr = [1, 11, 9, 2, 14, 7]
    n = len(arr)
    st = constructST(arr, n)
    print(st)
    print(arr)
    print('Sum: ', getSum(st, n, 1, 3))