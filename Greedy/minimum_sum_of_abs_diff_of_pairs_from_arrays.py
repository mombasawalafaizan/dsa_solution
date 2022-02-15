# Python3 program to find minimum sum 
# of absolute differences of two arrays.
def findMinSum(a, b, n):

	# Sort both arrays
	a.sort()
	b.sort()

	# Find sum of absolute differences
	sum = 0
	
	for i in range(n):
		sum = sum + abs(a[i] - b[i])

	return sum

# Driver program
	
# Both a[] and b[] must be of same size.
a = [4, 1, 8, 7]
b = [2, 3, 6, 5]
n = len(a)

print(findMinSum(a, b, n))

# This code is contributed by Anant Agarwal.
