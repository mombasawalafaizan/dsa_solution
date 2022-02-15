from collections import Counter

def possibleToRearrange(s: str)->int:
    '''Function answers whether rearrangement of string is possible such that no adjacent characters are same
    For that find the frequency of each character and find if satisfies the condition'''
    count = Counter(s)
    n = len(s)
    for ch in count:
        if n-count[ch]<count[ch]-1:
            return 0
    # Can also be done by this
    # maximum = max(count.values())
    # if (n%2==0 and maximum > n//2) or (n%2!=0 and maximum>(n+1)//2):
    #   return 0
    # else:
    #     return 1
    return 1
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(possibleToRearrange(s))