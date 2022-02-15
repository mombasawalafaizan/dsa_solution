'''https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/'''
from bisect import bisect_left, bisect_right

def noOfTriplets(arr:list, n:int, k:int):
    arr.sort()
    for i in range(n-1):
        for j in range(i+1, n):
            idx=BS_Left(arr, k-(arr[i]+arr[j]))
            if idx==-1:
                continue
            else:
                # If the current found element is i or j, then check for other 
                # duplicate element
                if idx==i or idx==j:
                    if BS_Right(arr, k-(arr[i]+arr[j]))!=idx:
                        return 1
                    continue    
                else:
                    return 1
    return 0
    
def BS_Left(a: list, x:int):
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

def BS_Right(a: list, x:int):
    i = bisect_right(a, x) 
    if i!=len(a)+1 and a[i-1] == x: 
        return (i-1) 
    else: 
        return -1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(noOfTriplets(arr, n, k))