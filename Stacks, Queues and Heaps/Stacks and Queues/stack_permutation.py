from collections import deque

def checkStackPermutation(inp, output):
    stack = deque()
    checker = deque()
    while output:
        to_check = output.popleft()
        if stack and to_check == stack[-1]:
            checker.append(stack.pop())
            continue
        elif inp:
            cur = inp.popleft()
            while to_check != cur:
                stack.append(cur)
                if not inp:
                    return False
                cur = inp.popleft()
            checker.append(cur)
        else:
            return False
    if not inp and not stack:
        return True
    else:
        return False

if __name__ == "__main__":
    inp = deque([1, 2, 3])
    out = deque([3, 1, 2])
    print(checkStackPermutation(inp, out))
    