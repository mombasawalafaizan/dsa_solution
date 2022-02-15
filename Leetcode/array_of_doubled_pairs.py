from collections import Counter
from bisect import bisect_left


class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        s = Counter(arr)
        # print(s)
        arr.sort()
        j = bisect_left(arr, 0)
        for i in range(j - 1, -1, -1):
            if arr[i] in s:
                s[arr[i]] -= 1
                if s[arr[i]] == 0:
                    del s[arr[i]]
                if not 2 * arr[i] in s:
                    return False
                s[2 * arr[i]] -= 1
                if s[2 * arr[i]] == 0:
                    del s[2 * arr[i]]

        for i in range(j, n):
            if arr[i] in s:
                s[arr[i]] -= 1
                if s[arr[i]] == 0:
                    del s[arr[i]]
                if not 2 * arr[i] in s:
                    return False
                s[2 * arr[i]] -= 1
                if s[2 * arr[i]] == 0:
                    del s[2 * arr[i]]
        return True


def canReorderDoubled(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    count = Counter(arr)
    for x in sorted(arr, key=abs):
        if count[x] == 0:
            continue
        if count[2 * x] == 0:
            return False
        count[x] -= 1
        count[2 * x] -= 1

    return True
