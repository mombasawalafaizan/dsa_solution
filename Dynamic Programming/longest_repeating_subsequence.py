def LRS(s: str) -> str:
    """Find the lowest common substring of the two strings passed"""
    n = len(s)
    # Create a (n+1) x (n+1) matrix
    matrix = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    i, j = n, n
    lcs = ""  # Lowest common substring
    while i != 0 and j != 0:
        if s[i - 1] == s[j - 1] and i != j:  # If common letter, go upper left
            lcs = s[i - 1] + lcs  # Store the letter in answer
            i -= 1
            j -= 1
        # Go vertical, if same or greater than horizontal value
        elif max(matrix[i - 1][j], matrix[i][j - 1]) == matrix[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return lcs


if __name__ == "__main__":
    s = input("Enter string: ")
    lcs = LRS(s)
    if lcs:
        print("\nLongest repeating:", lcs)
    else:
        print("\nNo repeating subsequence")
