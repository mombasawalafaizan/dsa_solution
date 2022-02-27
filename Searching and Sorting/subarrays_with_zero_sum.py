from collections import defaultdict


def findSubArrays(arr, n):
    found_sums = defaultdict(list)
    found_sums[0].append(-1)
    count = 0
    cur_sum = 0
    for i in range(n):
        cur_sum += arr[i]
        if cur_sum in found_sums:
            count += len(found_sums[cur_sum])
            for j in found_sums[cur_sum]:
                print(j + 1, i)
        found_sums[cur_sum].append(i)
    return count


def findSubArraysCnt(arr, n):
    found_sums = defaultdict(int)
    found_sums[0] = 1
    cnt, cur_sum = (0, 0)
    for i in range(n):
        cur_sum += arr[i]
        if cur_sum in found_sums:
            cnt += found_sums[cur_sum]
        found_sums[cur_sum] += 1
    return cnt
