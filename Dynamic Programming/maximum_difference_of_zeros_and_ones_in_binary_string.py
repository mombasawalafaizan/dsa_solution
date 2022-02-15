# My solution 
def maxSubstring(S):
    # code here
    max_diff = -1
    cur_diff = 0
    for i in range(len(S)):
        if S[i] == '0':
            cur_diff += 1
            max_diff = max(max_diff, cur_diff)
        elif cur_diff > 0:
            cur_diff -= 1
    return max_diff 

# Using Kadane's algorithm
def findLength(string, n): 
	current_sum = 0
	max_sum = 0

	# traverse a binary string from left 
	# to right 
	for i in range(n): 

		# add current value to the current_sum 
		# according to the Character 
		# if it's '0' add 1 else -1 
		current_sum += (1 if string[i] == '0' else -1) 

		if current_sum < 0: 
			current_sum = 0

		# update maximum sum 
		max_sum = max(current_sum, max_sum) 

	# return -1 if string does not contain 
	# any zero that means all ones 
	# otherwise max_sum 
	return max_sum if max_sum else -1