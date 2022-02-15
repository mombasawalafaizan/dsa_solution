# Approach: Initialize count = 0 and traverse the string character by character and keep track of the number of 0s and 1s so far,
# whenever the count of 0s and 1s become equal increment the count. If the count of 0s and 1s in the original string is not equal
# then print -1 else print the value of count after the traversal of the complete string.

def findSubStr(s: str)->int:
    cnt_zeros=0
    cnt_ones=0
    cnt=0
    i = 0
    for i in range(len(s)):
        if s[i]=='0':
            cnt_zeros+=1
        elif s[i]=='1':
            cnt_ones+=1
        if cnt_zeros==cnt_ones:
            cnt+=1

    if cnt_zeros==cnt_ones:
        return cnt
    else:
        return -1


if __name__ == "__main__":
    s = input('Enter binary string: ')
    print('Number of substrings with equal number of 0s and 1s:', findSubStr(s))