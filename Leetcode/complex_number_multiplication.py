# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3917/

def extractNumber(comp, start, last_char):
    i = start
    sign = 1
    if comp[i] == '-':
        sign = -1
        i += 1
    a = 0
    while comp[i] != last_char:
        a = a*10 + int(comp[i])
        i += 1
    return (sign*a, i)


def getRealImaginary(comp):
    a, i = extractNumber(comp, 0, '+')
    b, _ = extractNumber(comp, i+1, 'i')
    return (a, b)


def complexNumberMultiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    a, b = getRealImaginary(num1)
    c, d = getRealImaginary(num2)
    A = a*c - b*d
    B = a*d + b*c
    return str(A) + '+' + str(B) + 'i'
