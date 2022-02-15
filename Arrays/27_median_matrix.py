# First we find the minimum and maximum elements in the matrix. Minimum element can be easily found by comparing 
# the first element of each row, and similarly the maximum element can be found by comparing the last element of each row.
# Then we use binary search on our range of numbers from minimum to maximum, we find the mid of the min and max, 
# and get count of numbers less than our mid. And accordingly change the min or max.
# For a number to be median, there should be (r*c)/2 numbers smaller than that number. So for every number,
# we get the count of numbers less than that by using upper_bound() in each row of matrix, if it is less than the required count, 
# the median must be greater than the selected number, else the median must be less than or equal to the selected number.

from bisect import bisect_right

def binaryMedian(arr: list, r: int, c: int):
    mi = arr[0][0]
    mx = arr[0][c-1]
    for i in range(1, r):
        if arr[i][0] < mi:
            mi = arr[i][0]
        if arr[i][c-1] > mx:
            mx = arr[i][c-1]
    
    # Desired number of elements lesser and greater than median 
    desired=(r*c+1)//2 
    while mi < mx:
        place = 0
        mid = mi + (mx-mi)//2
        # Calculate the number of elements < mid
        for i in range(r):
            j = bisect_right(arr[i], mid)
            place = place + j
        if place < desired:
            mi = mid+1
        else:
            mx = mid
    return mi

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        arr = []
        for i in range(r):
            temp = list(map(int, input().split()))
            arr.append(temp)
        print('Median is:',binaryMedian(arr, r, c))