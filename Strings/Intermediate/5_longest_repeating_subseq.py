'''Same as longest repeating substring for two string, just a tweak that for the same string and
index of characters in two substrings should not be same'''

def printList(l):
    for i in l:
        print(i, end= ' ')
    print()

def findLongestRepeatingSubSeq(s: str): 
    n = len(s) 
    dp=[[0]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (s[i-1] == s[j-1] and i != j): 
                dp[i][j] = 1 + dp[i-1][j-1]         
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    printList([' ', ' ']+list(s))
    j = 0 
    for i in dp:
        if j > 0:
            printList([s[j]]+ i)
        else:
            printList([' '] + i)
        j += 1
    return dp[n][n]
        
if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(findLongestRepeatingSubSeq(s))