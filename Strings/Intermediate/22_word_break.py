# Recursive approach
# Done by Faizan
def possibleWordBreak(s, dictionary, start, end, n):
    if end==n:
        if (s[start:end] in dictionary):
            return True
        else:
            return False
    if s[start:end] in dictionary:
        return possibleWordBreak(s, dictionary, end, end+1, n)
    else:
        return possibleWordBreak(s, dictionary, start, end+1, n)



# Dynamic Programming solution with time complexity O(n*s) 
# where s is the length of the longest substring

# Returns true if string can be segmented into space 
# separated words, otherwise returns false 
def wordBreak(s: str, dictionary: set):
    n = len(s)
    if not s:
        return True
    # Create the DP table to store results of subproblems. 
	# The value dp[i] will be true if str[0..i] can be 
	# segmented into dictionary words, otherwise false.
    dp = [False] * (n+1)

    # matched_index array represents the indexes for which 
	# dp[i] is true. Initially only -1 element is present 
	# in this array.
    matched_index = [-1]
    for i in range(n):
        msize = len(matched_index)

        # Flag value which tells that a substring matches 
		# with given words or not. 
        flag = False
        for j in range(msize-1, -1, -1):

            # sb is substring starting from matched_index[j] + 1 to i(inclusive)
            sb = s[matched_index[j]+1: i+1]
            if sb in dictionary:
                flag = True
                break
        # If substring matches than do dp[i] = True and 
		# push that index in matched_index array. 
        if flag:
            dp[i]=True
            matched_index.append(i)
    
    return dp[n-1]
        
if __name__ == '__main__':
    # t = int(input())
    # for i in range(t):
    #     m = int(input())
    #     dictionary = set(input().split())
    #     s = input()
    #     n = len(s)
    #     print(int(possibleWordBreak(s, dictionary, 0, 1, n)))
    print(wordBreak('ilikesamsung', {"mobile", "samsung", "sam", 
				            "sung", "man", "mango", 
							"icecream", "and", "go", 
							"i", "like", "ice", "cream"}))
