# Another method is to generate two string with same length n one starting with 0 and 
# the other with 1, then check for the minimum flips with the generated strings and then
# original strings where conflict happens


# Done by Faizan
def minimumNumberOfBitFlips(s):
    '''Function to find minimum flips to convert the string into string with alternate digits'''
    c1_odd = 0
    c0_odd = 0
    c1_even = 0
    c0_even = 0
    for i in range(len(s)):
        if i%2==0:
            if s[i]=='1':
                c1_even+=1
            else:
                c0_even+=1
        else:
            if s[i]=='1':
                c1_odd+=1
            else:
                c0_odd+=1
    return min(c0_odd+c1_even, c0_even+c1_odd)
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(minimumNumberOfBitFlips(s))