def enqueue2stacks(s1, s2, el):
    s1.append(el)

def dequeue2stacks(s1, s2, el):
    if not s1 and not s2:
        return -1
    elif s1 and not s2:
        while s1:
            s2.append(s1.pop())
        return s2.pop()
    else:
        return s2.pop()

def enqueue1stack(s1, el):
    s1.append(el)

def dequeue1stack(s1):
    if not s1:
        return -1
    x = s1.pop()
    if not s1:
        return x
    item = dequeue1stack(s1)
    s1.append(x)
    return item