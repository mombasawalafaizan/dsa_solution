# Also LCS of string and reverse of string gives the longest
# palindromic subsequence

def lps(s):
    n = len(s)
    L = [[0 for _ in range(n)] for _ in range(n)]
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    # Build the table. Note that the lower 
    # diagonal values of table are
    # useless and not filled in the process. 
    # The values are filled in a
    # manner similar to Matrix Chain 
    # Multiplication DP solution (See
    # https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                L[i][j] = 2
            elif s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])

    print(list(range(len(s))))
    for i in L:
        print(i)
    i = 0
    j = n-1
    left = ''
    right = ''
    while True:
        if i==j:
            print(left+s[i]+right)
            break
        if (i+1)==j and s[i]==s[j]:
            print(left+s[i]+s[i]+right)
            break
        if s[i] == s[j]:
            left = left + s[i]
            right = s[i] + right
            i += 1
            j -= 1
        else:
            if L[i][j] == L[i][j-1]:
                j -= 1
            else:
                i += 1

    return L[0][n-1]

print(lps('riumuprr'))