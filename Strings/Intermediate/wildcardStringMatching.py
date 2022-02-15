def wildcardMatch(s1, s2):
    if len(s1)==0 and len(s2)==0:
        return True
    if len(s1) > 1 and s1[0] == '*' and len(s2)==0:
        return False
    if (len(s1)>1 and s1[0]=='?') or (len(s1) != 0 \
    and len(s2) !=0 and s1[0] == s2[0]):
        return wildcardMatch(s1[1:], s2[1:])
    if len(s1)!=0 and s1[0]=='*':
        return wildcardMatch(s1[1:], s2) or wildcardMatch(s1, s2[1:])
    return False

def wildcardMatchDP(s1, s2):
    r = len(s2)
    c = len(s1) 
    dp = [[False] * (c+1) for _ in range(r+1)]
    dp[0][0] = True
    for j in range(1, c+1):
        if s2[j-1]=='*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, r+1):
        for j in range(1, c+1):
            if s1[j-1]==s2[i-1] or s1[j-1]=='?':
                dp[i][j] = dp[i-1][j-1]
            if s1[j-1]=='*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[r][c]
        