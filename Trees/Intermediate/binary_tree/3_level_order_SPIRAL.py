from collections import deque
def findSpiral(root):
    if not root:
        return []
    dq = deque()
    stack_mode = True
    result = []
    dq.append(root)
    while dq:
        nodes_in_level = len(dq)
        while nodes_in_level>0:
            if stack_mode:
                cur_node = dq.pop()
            else:
                cur_node = dq.popleft()     
            result.append(cur_node.data)
            if stack_mode:
                if cur_node.right:
                    dq.appendleft(cur_node.right)
                if cur_node.left:
                    dq.appendleft(cur_node.left)
            else:
                if cur_node.left:
                    dq.append(cur_node.left)
                if cur_node.right:
                    dq.append(cur_node.right)
            nodes_in_level-=1
        stack_mode = not stack_mode
    return result