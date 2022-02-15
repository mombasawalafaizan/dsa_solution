def maxAbsDiff(arr, n):
    max_diff = 0
    arr.sort()
    i = 0
    j = n-1
    while i<=j:
        # 
        if i==j:
            max_diff += abs(arr[j]-arr[0])
            break
        max_diff += abs(arr[i]-arr[j])
        if j-i == 1:
            max_diff += abs(arr[j] - arr[0])
        else:
            max_diff += abs(arr[j] - arr[i+1])
        i += 1
        j -=1
    return max_diff

if __name__ == '__main__':
    arr = [1, 2, 4, 8]
    print(maxAbsDiff(arr, len(arr)))