from collections import Counter

def secondMostRepeatedString(s):
    count = Counter(s)
    i = 1
    while s[i]==s[0]:
        i+=1
    max1 = max(count[s[0]], count[s[i]])
    max2 = min(count[s[0]], count[s[i]])
    
    for word in count:
        if count[word] > count[max1]:
            max2 = max1
            max1 = word
        elif count[word] > count[max2]:
            max2 = word
    return max2
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        s = input().split()
        print(secondMostRepeatedString(s))