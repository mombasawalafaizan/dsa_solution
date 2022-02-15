def LCS(s1: str, s2: str) -> str:
    """Find the lowest common substring of the two strings passed"""
    m = len(s1)
    n = len(s2)
    # Create a (m+1) x (n+1) matrix
    matrix = [[0]*(n+1) for i in range(m+1)] 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    i, j = m, n
    lcs = '' #Lowest common substring
    while i!=0 and j!=0:
        if s1[i-1]==s2[j-1]: #If common letter, go upper left
            lcs = s1[i-1] + lcs #Store the letter in answer
            i-=1
            j-=1
        #Go vertical, if same or greater than horizontal value
        elif max(matrix[i-1][j], matrix[i][j-1]) == matrix[i-1][j]:
            i-=1
        else:
            j-=1
    return lcs

if __name__ == '__main__':
    s1 = input('Enter first string: ')
    s2 = input('Enter second string: ')
    lcs = LCS(s1, s2)
    if lcs:
        print('\nLongest common substring of',s1,'and',s2,'\b:',lcs)
    else:
        print('\nNo common substring found between',s1,'and',s2,'\b.')