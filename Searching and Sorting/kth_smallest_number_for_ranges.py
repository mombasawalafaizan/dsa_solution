def find_smallest_gte_el(arr, n, x):
    '''Finds the smallest greater than or equal to element for x'''
    l = 0
    h = n-1
    while l <= h:
        mid = (l+h)//2
        if x > arr[mid][2]:
            l = mid + 1
        else:
            if mid==0 or arr[mid][2]==x or \
                x > arr[mid-1][2] :
                return mid
            h = mid
    return -1


# Write your code here
def merge_intervals(arr):
    arr.sort()
    idx = 0
    for i in range(1, len(arr)):
        if arr[i][0]<=arr[idx][1]:
            arr[idx][1] = max(arr[idx][1], arr[i][1])
            if idx!=0:
                arr[idx][2] = arr[idx][1] - arr[idx][0] + arr[idx-1][2] + 1
            else:
                arr[idx][2] = arr[idx][1] - arr[idx][0] + 1
        else:
            idx += 1
            arr[idx] = arr[i]
            arr[idx][2] = arr[idx][1] - arr[idx][0] + arr[idx-1][2] + 1
    return arr[:idx+1]
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        temp = []
        for _ in range(n):
            a, b = map(int, input().split())
            temp.append([a,b,b-a+1])
        ranges = merge_intervals(temp)
        num = len(ranges)
        for _ in range(q):
            k = int(input())
            cur_idx = find_smallest_gte_el(ranges, num, k)
            if cur_idx == -1:
                print(-1)
            else:
                if cur_idx != 0:
                    cur_range_len = k-ranges[cur_idx-1][2]
                else:
                    cur_range_len = k
                print(ranges[cur_idx][0] + cur_range_len - 1)