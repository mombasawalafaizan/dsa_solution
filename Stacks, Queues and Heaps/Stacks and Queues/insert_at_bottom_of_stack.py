from collections import deque
def insert_at_bottom(stack, el):
    if not stack:
        stack.append(el)
    else:
        top = stack.pop()
        insert_at_bottom(stack, el)
        stack.append(top)

stack = [2, 3, 12, 4, 5]
insert_at_bottom(stack, 4)
print(stack)