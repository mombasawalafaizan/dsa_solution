# Another good algorithm with O(n) time and O(1) space complexity
def swapCount(s): 
    chars = s
    # Stores total number of left and  
    # right brackets encountered 
    countLeft = 0
    countRight = 0
    # Swap stores the number of swaps  
    # required imbalance maintains the
    # number of imbalance pair 
    swap = 0
    imbalance = 0; 
    for i in range(len(chars)):
        if chars[i] == '[':
            # Increment count of left bracket
            countLeft += 1
            if imbalance > 0:
                # Swaps count is last swap 
                # count + total number 
                # imbalanced brackets 
                swap += imbalance
                # Imbalance decremented by 1
                # as it solved only one 
                # imbalance of left and right 
                imbalance -= 1
                
        elif chars[i] == ']':
            # Increment count of right bracket 
            countRight += 1
            # Imbalance is reset to current
            # difference between left and 
            # right brackets 
            imbalance = (countRight - countLeft) 

    return swap


def makeBalanced(s:list, n:int)->int:
    pos = [i for i in range(n) if s[i]=='['] # Positions of opening brackets
    swaps = 0
    p = 0
    count = 0
    for i in range(n):
        if s[i]=='[':
            count += 1
            p += 1
        elif s[i]==']':
           count -= 1
        # If imbalance occurs, get the next opening bracket position
        if count<0:
            swaps += pos[p]-i
            s[pos[p]], s[i] = s[i], s[pos[p]]
            p += 1
            count = 1
    return swaps
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(makeBalanced(list(s), n))