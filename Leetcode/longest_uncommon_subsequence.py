class Solution(object):
    def isSubsequence(self, s, t):
        """Function to find whether """
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=lambda x: -len(x))
        # strs.sort(key = lambda x: len(x), reverse=True)
        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i != j and self.isSubsequence(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1

    # Just a function to find longest uncommon subsequence in two strings
    def LUS_in_2_strings(self, s1, s2):
        return max(len(s1), len(s2)) if s1 != s2 else -1
