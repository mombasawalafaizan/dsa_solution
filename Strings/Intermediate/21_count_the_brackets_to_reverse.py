from collections import deque

# GEEKS FOR GEEKS SOLUTION
# Returns count of minimum reversals  
# for making expr balanced. Returns -1  
# if expr cannot be balanced.  
def countMinReversals(expr):
    # Remove the balanced string from the given string and then 
    # calculate the number of changes required by the swap formula
    # which is ceil(n/2) + ceil(m/2) where n and m are number of opening 
    # and closing brackets
    lenn = len(expr)  
  
    # length of expression must be even  
    # to make it balanced by using reversals.  
    if (lenn % 2) : 
        return -1
  
    # After this loop, stack contains  
    # unbalanced part of expression,   
    # i.e., expression of the form "...."  
    s = deque()
    for i in range(lenn): 
        if (expr[i] =='}' and s):  
            if (s[-1] == '{'): 
                s.pop()  
            else: 
                s.append(expr[i])  
        else: 
                s.append(expr[i])  
      
    # Length of the reduced expression  
    # red_len = (m+n)  
    red_len = len(s)  
    # count opening brackets at the  
    # end of stack  
    n = 0
    while s and s[-1]=='{' : 
        s.pop()  
        n += 1
  
    # return ceil(m/2) + ceil(n/2) which 
    # is actually equal to (m+n)/2 + n%2  
    # when m+n is even.  
    return (red_len // 2 + n % 2)  

# Done by Faizan
def makeBalanced(s):
    n = len(s)
    if n%2!=0:
        return -1
    s1 = deque() # Stack for storing opening brackets
    s2 = deque() # Stack for storing closing brackets (maximum 1 can be stored)
    change = 0
    for ch in s:
        if ch == '{':
            s1.append(ch)
        elif s1: # If closing bracket results in a balanced expression, get rid of it
            s1.pop()
        elif s2: # If there is a previous closing bracket, make change of 1
            s2.pop()
            change+=1
        else: # Store if not possible to change
            s2.append(ch)

    # If case like }}{{{{, get rid of 2 opening and 2 closing brackets by reversing them
    while s1 and s2: 
        s1.pop()
        s2.pop()
        change+=2
    change+=(len(s1)//2 + len(s2)//2)
    return change
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(countMinReversals(s))