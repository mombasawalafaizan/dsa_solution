# i is the starting index and j is the ending index. i must be passed as 0 and j as n-1
# minPalPartion(str, i, j) = 0 if i == j.  When string is of length 1.
# minPalPartion(str, i, j) = 0 if str[i..j] is palindrome.

# If none of the above conditions is true, then minPalPartion(str, i, j) can be 
# calculated recursively using the following formula.
# minPalPartion(str, i, j) = Min { minPalPartion(str, i, k) + 1 + minPalPartion(str, k+1, j) } 
#                            where k varies from i to j-1

# Time complexity is O(n^3)
def minPalPartion(str):
	
	# Get the length of the string
	n = len(str)
	
	# Create two arrays to build the
	# solution in bottom up manner
	# C[i][j] = Minimum number of cuts
	# needed for palindrome
	# partitioning of substring str[i..j]
	# P[i][j] = true if substring str[i..j]
	# is palindrome, else false. Note that
	# C[i][j] is 0 if P[i][j] is true
	C = [[0 for i in range(n)]
			for i in range(n)]
	P = [[False for i in range(n)]
				for i in range(n)]

	# different looping variables
	j = 0
	k = 0
	L = 0
	
	# Every substring of length
	# 1 is a palindrome
	for i in range(n):
		P[i][i] = True
		C[i][i] = 0
		
	# L is substring length. Build the
	# solution in bottom-up manner by
	# considering all substrings of
	# length starting from 2 to n.
	# The loop structure is the same as
	# Matrix Chain Multiplication problem
	for L in range(2, n + 1):
		
		# For substring of length L, set
		# different possible starting indexes
		for i in range(n - L + 1):
			j = i + L - 1 # Set ending index
			
			# If L is 2, then we just need to
			# compare two characters. Else
			# need to check two corner characters
			# and value of P[i + 1][j-1]
			if L == 2:
				P[i][j] = (str[i] == str[j])
			else:
				P[i][j] = ((str[i] == str[j]) and
							P[i + 1][j - 1])
							
			# IF str[i..j] is palindrome,
			# then C[i][j] is 0
			if P[i][j] == True:
				C[i][j] = 0
			else:
				
				# Make a cut at every possible
				# location starting from i to j,
				# and get the minimum cost cut.
				C[i][j] = 10**7
				for k in range(i, j):
					C[i][j] = min (C[i][j], C[i][k] +
								C[k + 1][j] + 1)
									
	# Return the min cut value for
	# complete string. i.e., str[0..n-1]
	return C[0][n - 1]

# O(n^2) solution 
def minCut(a):
 
    cut = [0 for i in range(len(a))]
    palindrome = [[False for i in range(len(a))] for j in range(len(a))]
    for i in range(len(a)):
        minCut = i
        for j in range(i + 1):
            if (a[i] == a[j] and (i - j < 2 or palindrome[j + 1][i - 1])):      
                palindrome[j][i] = True
                minCut = min(minCut,0 if  j == 0 else (cut[j - 1] + 1))
        cut[i] = minCut  
    return cut[len(a) - 1]

# Driver code
str = "ababbbabbababa"
print ('Min cuts needed for Palindrome Partitioning is', minPalPartion(str))
									