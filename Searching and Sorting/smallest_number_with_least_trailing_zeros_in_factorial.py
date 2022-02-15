# Python3 program tofind smallest 
# number whose 
# factorial contains at least 
# n trailing zeroes 

# Return true if number's factorial contains 
# at least n trailing zero else false. 
def check(p,n): 

	temp = p 
	count = 0
	f = 5
	while (f <= temp): 
		count += temp/f 
		f = f*5

	return (count >= n) 

# Return smallest number whose factorial 
# contains at least n trailing zeroes 
def findNum(n): 

	# If n equal to 1, return 5. 
	# since 5! = 120. 
	if (n==1): 
		return 5

	# Initalizing low and high for binary 
	# search. 
	low = 0
	high = 5*n 

	# Binary Search. 
	while (low <high): 

		mid = (low + high) >> 1

		# Checking if mid's factorial contains 
		# n trailing zeroes. 
		if (check(mid, n)): 
			high = mid 
		else: 
			low = mid+1
	

	return low 


# driver code 
n = 6
print(findNum(n)) 
