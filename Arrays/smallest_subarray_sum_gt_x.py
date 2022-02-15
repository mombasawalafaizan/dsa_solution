# Both the below functions work in O(n) time complexity
# GFG version is more underestandable

# Faizan's version
def minSubarrGtX(arr, n, x):
    if n==1:
        return 1
    left, right = 0, 1
    cur_sum = arr[0]
    min_length = n + 1
    while right < n or cur_sum > x:
        if cur_sum > x:
            min_length = min(min_length, right-left)
            cur_sum -= arr[left]
            left+=1
            if left>right:
                return 1
        else:
            cur_sum += arr[right]
            if right < n:
                right += 1
            else:
                cur_sum -= arr[left]
                left += 1
    return min_length if min_length!=n+1 else -1        

# GFG version 
def smallestSubWithSum(arr, n, x): 
  
    # Initialize current sum and minimum length 
    curr_sum = 0
    min_len = n + 1
  
    # Initialize starting and ending indexes 
    start = 0
    end = 0
    while (end < n): 
      
        # Keep adding array elements while current 
        # sum is smaller than x 
        while (curr_sum <= x and end < n): 
            curr_sum += arr[end] 
            end+= 1
  
        # If current sum becomes greater than x. 
        while (curr_sum > x and start < n): 
          
            # Update minimum length if needed 
            if (end - start < min_len): 
                min_len = end - start  
  
            # remove starting elements 
            curr_sum -= arr[start] 
            start+= 1
      
    return min_len  

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        print(minSubarrGtX(arr, n, x))