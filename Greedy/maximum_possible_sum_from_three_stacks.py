from collections import deque

def findSumOfStack(stack):
    if len(stack)==0:
        return 0
    x = stack.pop()
    temp = x + findSumOfStack(stack)
    stack.append(x)
    return temp

def maxEqualSum(s1, s2, s3):
    sum1 = findSumOfStack(s1)
    sum2 = findSumOfStack(s2)
    sum3 = findSumOfStack(s3)
    while s1 and s2 and s3:
        if sum1 == sum2 and sum2 == sum3:
            return sum1
        if (sum1 >= sum2 and sum1 >= sum3):
            temp = s1.pop()
            sum1 -= temp
        elif (sum2 >= sum1 and sum2 >= sum3):
            temp = s2.pop()
            sum2 -= temp
        else: 
            temp = s3.pop()
            sum3 -= temp
    return 0            

if __name__ == '__main__':
    stack1 = deque([1, 1, 1, 2, 3])
    stack2 = deque([2, 3, 4])
    stack3 = deque([1, 4, 1, 1])
    print(maxEqualSum(stack1, stack2, stack3))