def findMaxSum(arr1, n1, arr2, n2): 
    i = 0
    j = 0
    cur_sum1 = 0
    cur_sum2 = 0
    prev1 = 0
    prev2 = 0
    maxlen = 0
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            cur_sum1 += arr1[i]
            cur_sum2 += arr2[j]
            maxlen += max(cur_sum1 - prev1, cur_sum2 - prev2)
            prev1 = cur_sum1
            prev2 = cur_sum2
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            cur_sum1 += arr1[i]
            i += 1
        else:
            cur_sum2 += arr2[j]
            j += 1

    while i < n1:
        cur_sum1 += arr1[i]
        i += 1
    while j < n2:
        cur_sum2 += arr2[j]
        j += 1
    maxlen += max(cur_sum1 - prev1, cur_sum2 - prev2)
    return maxlen


if __name__ == "__main__":
    while True:
        s1 = list(map(int, input().strip().split()))
        n1 = s1[0]
        if n1 == 0:
            break
        arr1 = s1[1:]
        s2 = list(map(int, input().strip().split()))
        n2 = s2[0]
        arr2 = s2[1:]
        # print(arr1, n1)
        # print(arr2, n2)
        print(findMaxSum(arr1, n1, arr2, n2))