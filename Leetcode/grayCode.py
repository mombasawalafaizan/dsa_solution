from pprint import List

# The logic is to first start with 0 and then mirror it, hence for each iteration
# we'll mirror(reverse the list and append it to last) and add 1 to the MSB


def grayCode(n: int) -> List[int]:
    """ This function returns the gray-code list for n bits """
    res = [0] * 2**n
    k = 0
    while k < n:
        j = (1 << (k+1)) - 1
        p = 0
        while p < j:
            res[j] = res[p]
            res[j] = res[j] | (1 << k)
            j -= 1
            p += 1
        k += 1
    return res
