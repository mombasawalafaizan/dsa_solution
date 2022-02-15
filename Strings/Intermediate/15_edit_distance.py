'''Same as Longest Common Subsequence problem but conditions are different'''

# Example:
# First create a dp array with the below initial values
#   $ g e s e k
# $ 0 1 2 3 4 5
# g 1 0 0 0 0 0
# e 2 0 0 0 0 0
# e 3 0 0 0 0 0
# k 4 0 0 0 0 0
# Then, if character is same, then get no dp[i][j] = dp[i-1][j-1]
# else it is the (minimum of up, left and diagonal) + 1
#   $ g e s e k
# $ 0 1 2 3 4 5
# g 1 0 1 2 3 4
# e 2 1 0 1 2 3
# e 3 2 1 1 1 2
# k 4 3 2 2 2 1

def editDistance(s1: str, p: int, s2: str, q: int)->int:
    dp = [[0]*(q+1) for i in range(p+1)]
    for i in range(1, q+1):
        dp[0][i] = i
    for i in range(1, p+1):
        dp[i][0] = i
    
    for i in range(1,p+1):
        for j in range(1,q+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
    
    return dp[p][q]
        
if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n1, n2 = map(int, input().split())
        s1, s2 = input().split()
        print(editDistance(s1, n1, s2, n2))