from collections import deque

def checkRedundancy(s):
    stack = deque()
    for ch in s:
        if ch == ')':
            top = stack.pop()
            flag = True
            while top!='(':
                if top in {'+', '-', '*', '/'}:
                    flag = False
                top = stack.pop()
            if flag:
                return True
        else:
            stack.append(ch)
    return False