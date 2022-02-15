'''def findLongestConseqSubseq(arr, n): 
  
    s = Set() 
    ans = 0
  
    # Hash all the array elements 
    for ele in arr: 
        s.add(ele) 
  
    # check each possible sequence from the start 
    # then update optimal length 
    for i in range(n): 
  
         # if current element is the starting 
        # element of a sequence 
        if (arr[i]-1) not in s: 
  
            # Then check for next elements in the 
            # sequence 
            j = arr[i] 
            while(j in s): 
                j+= 1
  
            # update  optimal length if this length 
            # is more 
            ans = max(ans, j-arr[i]) 
    return ans '''    
def findMaxConsecutiveSequence(n:int, arr:list) -> int:
    arr.sort()
    longest = 1
    i = 0
    while i < n-1:
        cur_max = 1
        while i<n-1 and (arr[i+1]-arr[i]) <= 1:
            if arr[i+1]-arr[i] != 0:
                cur_max += 1
            i += 1
        if cur_max > longest:
            longest = cur_max
        i += 1
    return longest
            
    
    
if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        a = list(map(int, input().split()))
        print(findMaxConsecutiveSequence(n, a))