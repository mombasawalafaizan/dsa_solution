from collections import deque, OrderedDict

#  While stack and Queue is not empty.
#  a = top element of stack;
#  b = front of queue;
#  if (a != b)
#    return false;
#  pop element from stack and queue.

def mirrorUtil(tree1, tree2):
    for i in range(1, len(tree1)):
        stack = tree1[i]
        queue = tree2[i]
        while stack and queue:
            if stack[-1] != queue[0]:
                return False
            stack.pop()
            queue.popleft()
        if stack or queue:
            return False
    return True
        
def mirrorTree(n, e, set1, set2):
    tree1 = [deque() for i in range(n+1)]
    tree2 = [deque() for i in range(n+1)]

    for i in range(0, 2*e, 2):
        tree1[int(set1[i])].append(set1[i+1])
        
    for i in range(0, 2*e, 2):
        tree2[int(set2[i])].append(set2[i+1])

    print(tree1)
    print(tree2)    
    return int(mirrorUtil(tree1, tree2))

# Note: Nodes are inputted from 1 to n

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, e = map(int, input().split())
        set1 = input().split()
        set2 = input().split()
        print(mirrorTree(n, e, set1, set2))