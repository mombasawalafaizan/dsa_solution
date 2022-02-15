# See this to understand the concepts:
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/

def longestSubstring(s: str, k: int) -> int:
    maxUnique = len(set(s))
    result = 0

    for currUnique in range(1, maxUnique + 1):
        countMap = [0] * 26
        st, end, unique, countAtLeastK = (0, 0, 0, 0)
        while end < len(s):
            if unique <= currUnique:
                idx = ord(s[end]) - ord('a')
                if countMap[idx] == 0:
                    unique += 1
                countMap[idx] += 1
                if countMap[idx] == k:
                    countAtLeastK += 1
                end += 1
            else:
                idx = ord(s[st]) - ord('a')
                if countMap[idx] == k:
                    countAtLeastK -= 1
                countMap[idx] -= 1
                if countMap[idx] == 0:
                    unique -= 1
                st += 1
            if unique == currUnique and unique == countAtLeastK:
                result = max(end - st, result)
    return result
