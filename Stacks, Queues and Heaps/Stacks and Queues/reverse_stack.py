from collections import deque

def insertAtBottom(stack, el):
    if not stack:
        stack.append(el)
    else:
        top = stack.pop()
        insertAtBottom(stack, el)
        stack.append(top)

def reverse(stack):
    if stack:
        temp = stack.pop()
        reverse(stack)
        insertAtBottom(stack, temp)


stack = deque([3, 4, 2, 5])
reverse(stack)
print(stack)