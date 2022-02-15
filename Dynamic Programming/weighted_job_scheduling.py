from collections import namedtuple

Job = namedtuple('Job', ['start', 'finish', 'profit'])

def latestNonConflictBS(self, arr, i):
    # Takes O(lg n) time, binary search
    l, h = 0, i-1
    st = arr[i][0]
    while (h-l)>1:
        mid = (l+h)//2
        if arr[mid][1] <= st:
            l = mid
        else:
            h = mid - 1
    if st >= arr[h][1]:
        return h
    elif st >= arr[l][1]:
        return l
    return -1
    
def latestNonConflict(arr, idx):
    # Takes O(n) time, linear search
    for j in range(idx-1, -1, -1):
        if arr[idx].start >= arr[j].finish:
            return j
    return -1


def findMaxProfit(arr, n):
    arr.sort(key = lambda x: x.finish)
    dp = [i.profit for i in arr]
    for i in range(1, n):
        l = latestNonConflict(arr, i)
        if l!=-1:
            dp[i] += dp[l]
        dp[i] = max(dp[i-1], dp[i])
    return dp[n-1]

if __name__ == '__main__':
    jobs = []
    jobs.append(Job(3, 10, 20))
    jobs.append(Job(1, 2, 50))
    jobs.append(Job(6, 19, 100))
    jobs.append(Job(2, 100, 200))
    print(findMaxProfit(jobs, len(jobs)))
