import bisect 

''' 
Function to Generate all subsets of a set 
	start --> Starting Index of the Set for the 
		first/second half Set 
	setSize --> Number of element in half Set 
	S --> Original Complete Set 
	res --> Store the subsets sums 
'''
def generateSubsets(start, setSize, S, res): 
	
	# setSize of power set of a set with setSize 
	# N is (2^n - 1) 
	pow_setSize = pow(2, setSize) 

	# Store the sum of particular subset of set 
	add = 0

	# Run from counter 000..0 to 111..1 
	for counter in range(pow_setSize): 
		
		# set the sum initially to zero 
		add = 0

		for j in range(setSize): 
			
			# Check if jth bit in the counter is set 
			# If set then pront jth element from set 
			if counter & (1 << j): 
				add += S[j + start] 

		# Store the sum in a vector 
		res.append(add) 
		
def numberOfSubsets(S, N, A, B): 

	# Vectors to store the subsets sums 
	# of two half sets individually 
	S1 = [] 
	S2 = [] 

	# Generate subset sums for the first half set 
	generateSubsets(0, N // 2, S, S1) 

	# Generate subset sums for the second half set 
	if (N % 2 != 0): 
		generateSubsets(N // 2, 
						N // 2 + 1, S, S2) 
	else: 
		generateSubsets(N // 2, 
						N // 2, S, S2) 

	# Sort the second half set 
	S2.sort() 

	# Number of required subsets 
	# with desired Sum 
	ans = 0

	for i in range(len(S1)): 

		# Search for lower bound 
		low = bisect.bisect_left(S2, A - S1[i]) 

		# Search for upper bound 
		high = bisect.bisect_right(S2, B - S1[i]) 

		# Add up to get the desired answer 
		ans += (high - low) 

	return ans 

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(numberOfSubsets(arr, n, a, b))