from typing import OrderedDict
from collections import OrderedDict, defaultdict

def findMinKey(d: dict)->str:
    '''Function to find key with minimum value'''
    min_val=float('inf')
    min_key=None
    for i in d:
        if d[i]!=-1 and d[i]<min_val:
            min_val=d[i]
            min_key=i
    
    return min_key
def minSubstringWithDistinctChar(s: str)->str:
    '''Finding the minimum substring with distinct characters'''
    n = len(s)
    # distinct=OrderedDict({i:-1 for i in set(s)})
    distinct={i:-1 for i in set(s)} # A dictionary which will store the latest position of each character
    # distinct=OrderedDict({i:-1 for i in set(s)}) # In case of OrderedDict
    distinct_char=len(distinct) # Number of distinct characters
    min_len = float('inf') # The minimum length of the substring to be returned
    distinct_chars_traversed = 0 
    prev_min_char = s[0] # The newest character from which the current substring is started

    for i in range(n):
        # Increment the number of distinct characters traversed
        if distinct[s[i]]==-1:
            distinct_chars_traversed+=1
        distinct[s[i]]=i # Store the latest index
        # distinct.move_to_end(s[i]) # In case of OrderedDict
        # If the current character is the same character from which the substring started,
        # find the next character from which the substring could start
        if s[i]==prev_min_char:
            prev_min_char = findMinKey(distinct)
            # prev_min_char = next(iter(distinct.items()))[0] # In case of OrderedDict
        # Find the minimum length substring
        if distinct_chars_traversed==distinct_char and min_len>(i-distinct[prev_min_char]+1):
            min_len=i-distinct[prev_min_char]+1
            # In case if smallest possible substring is found, return it
            # to avoid further processing
            if min_len==distinct_chars_traversed:
                return min_len
    return min_len

# Function to find smallest window 
# containing all distinct characters 
def findSubString(strr): 
	
	n = len(strr) 
	
	# Count all distinct characters. 
	dist_count = len(set([x for x in strr])) 
	
	curr_count = defaultdict(lambda: 0) 
	count = 0
	start = 0
	min_len = n 
	start_index = 0
	# Now follow the algorithm discussed in below 
	# post. We basically maintain a window of characters 
	# that contains all characters of given string. 
	for j in range(n): 
		curr_count[strr[j]] += 1
		
		# If any distinct character matched, 
		# then increment count 
		if curr_count[strr[j]] == 1: 
			count += 1
			
		# Try to minimize the window i.e., check if 
		# any character is occurring more no. of times 
		# than its occurrence in pattern, if yes 
		# then remove it from starting and also remove 
		# the useless characters. 
		if count == dist_count: 
			while curr_count[strr[start]] > 1: 
				if curr_count[strr[start]] > 1: 
					curr_count[strr[start]] -= 1
					
				start += 1
				
			# Update window size 
			len_window = j - start + 1
			
			if min_len > len_window: 
				min_len = len_window 
				start_index = start 

	# Return substring starting from start_index 
	# and length min_len """ 
	return str(strr[start_index: start_index + min_len]) 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(minSubstringWithDistinctChar(s))