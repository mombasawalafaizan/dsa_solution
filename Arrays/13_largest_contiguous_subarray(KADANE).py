'''
KADANE'S ALGORITHM
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far'''

# Python program to find maximum contiguous subarray 

# Function to find the maximum contiguous subarray 

def maxSubArraySum(a,size): 
	
	max_so_far = float('-inf')
	max_ending_here = 0
	
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if (max_so_far < max_ending_here): 
		  max_so_far = max_ending_here 

		if max_ending_here < 0: 
		  max_ending_here = 0
	return max_so_far 

# Driver function to check the above function 
if __name__=='__main__':
  a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
  print("Maximum contiguous sum is", maxSubArraySum(a,len(a)) )

#This code is contributed by _Devesh Agrawal_ 

