def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ''
    
    L = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    max_len = 1
    st = 0
    end = 0
    for sep in range(2, n+1):
        for i in range(n-sep+1):
            j = i + sep - 1
            if s[i]==s[j]:
                if sep==2:
                    L[i][j] = 2
                elif L[i+1][j-1]!=0:
                    L[i][j] = L[i+1][j-1] + 2
                if L[i][j] > max_len:
                    st = i
                    end = j
                    
    # for i in L:
    #     print(i)
    return s[st:end+1]