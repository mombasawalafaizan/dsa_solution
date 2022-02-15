# IMPORTANT:The below solution discussed handles the case for duplicate characters also

# Returns true if str[curr] does not 
# matches with any of the characters 
# after str[start] 
def shouldSwap(string, start, curr): 

	for i in range(start, curr): 
		if string[i] == string[curr]: 
			return 0
	return 1

# Prints all distinct permutations 
# in str[0..n-1] 
def findPermutations(arr, string, index, n): 

	if index >= n: 
		arr.append(''.join(string)) 
		return

	for i in range(index, n): 

		# Proceed further for str[i] only 
		# if it doesn't match with any of 
		# the characters after str[index] 

        # (Drop the below 2 lines of code if distinct characters are there in string)
		check = shouldSwap(string, index, i) 
		if check: 
			string[index], string[i] = string[i], string[index] 
			findPermutations(arr, string, index + 1, n) 
			string[index], string[i] = string[i], string[index] 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = list(input())
        arr = []
        findPermutations(arr, s, 0, len(s))
        # Just to print in sorted order as per program requirements
        for i in sorted(arr):
            print(i, end=' ')
        print()