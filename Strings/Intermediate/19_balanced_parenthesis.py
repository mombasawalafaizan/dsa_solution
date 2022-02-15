from collections import deque
def balancedParenthesis(s: str)-> str:
    stack = deque()
    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        else:
            if stack:
                popped = stack.pop()
                if (ch == ')' and popped!='(') or  (ch == '}' and popped!='{') or (ch == ']' and popped!='['):
                    return 'not balanced'
            else:
                return 'not balanced'
    if stack:
        return 'not balanced'
    return 'balanced'
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(balancedParenthesis(s))