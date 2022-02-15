from bisect import bisect_right

# There are N piles of coins each containing  Ai (1<=i<=N) coins.  
# Now, you have to adjust the number of coins in each pile such that for any two pile, 
# if a be the number of coins in first pile and b is the number of coins in second pile
# then |a-b|<=K. In order to do that you can remove coins from different piles to decrease
# the number of coins in those piles but you cannot increase the number of coins in a pile 
# by adding more coins. Now, given a value of N and K, along with the sizes of the N different
# piles you have to tell the minimum number of coins to be removed in order to satisfy the given condition.


# NOTE: You can also remove a pile by removing all the coins of that pile. This
# means that you just add the number of coins in pile you have removed and treat the
# remaining problem as separate
# If the above condition is not there, below is the required function
# 
# def coinPiles(arr, n, k):
#     min_cost = 0
#     minValue = min(arr)
#     for i in range(n):
#         if arr[i] > (minValue + k):
#             min_cost += (arr[i] - (minValue + k))
#     return min_cost

def coinPiles(arr, n, k):
    arr.sort()
    p = [0] * n
    p[0] = arr[0]
    for i in range(1, n):
        p[i] = p[i-1] + arr[i]
    ans, prev = float('inf'), 0
    for i in range(n):
        # Find the position of value from which uptil end the condition does not satisfy
        pos = bisect_right(arr, arr[i]+k, i, n)
        # Remove the current pile if value is changed
        if i>0 and arr[i]!=arr[i-1]: prev = p[i-1]
        # Add the cost of removing previous values and for range from [pos, n) we can find their
        # sum from prefix sum array and remove the required minimum value from them, hence
        # we can get the extra coins
        ans = min(ans, prev+(p[n-1]-p[pos-1])-(n-pos)*(arr[i]+k))
    return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(coinPiles(arr, n, k))