def LPS(s: str)->str:
    '''This functions finds the longest palindromic substring from the given string, in O(n*n) time complexity'''
    n = len(s)
    min_idx = 0
    max_idx = 0
    for k in range(n):
        start=k # Check for maximum palindromic substring from start point
        end=n-1 # Start searching from the last element
        while end>start: 
            # If a character matches, check if it is palindrome
            # If not make end point to position where it fails
            if s[start]==s[end]: 
                i, j = start+1, end-1
                while i<j:
                    if s[i]!=s[j]:
                        end=j+1
                        break
                    i+=1
                    j-=1
                # Check whether it is greater than the previous longest found string
                if i>=j and (end-start)>(max_idx-min_idx): 
                    min_idx=start
                    max_idx=end
            start=k    
            end-=1
    return s[min_idx:max_idx+1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(LPS(s))    