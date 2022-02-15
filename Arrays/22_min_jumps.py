'''#Refere GFG for recursive and DP approach both in O(n^2) only same as my approach
https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
'''
# Approach done by FAIZAN, GREEDY APPROACH
def minimumJumps(arr: list, n: int) -> int:
    jumps = 0
    i = 0
    while i<n-1:
        idx=i
        possibilities=i+arr[i] # Minimum possibilities to start with
        if possibilities >= n-1: # If possibilities reach the end, then jump to the end
            jumps+=1
            break
        # Check for the best possibility(max(j+arr[j])) to consider
        for j in range(i+1, i+arr[i]+1):
            # If any possibility reach the end, then take it
            if j+arr[j]>=n-1:
                idx=j
                break
            if j+arr[j]>possibilities:
                idx=j
                possibilities=j+arr[j]
        # If you can go nowhere from here, quit
        if idx==i:
            return -1
        # Jump to the next index with the most possibilities
        i=idx
        jumps+=1
    return jumps

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(minimumJumps(arr, n))
