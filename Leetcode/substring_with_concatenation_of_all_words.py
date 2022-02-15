# You are given a string s and an array of strings words of the same length. Return all starting indices
#  of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without
#  any intervening characters.
# You can return the answer in any order.

# eg.
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
from collections import Counter


def findSubstringGeneral(s, words):
    """
        This function is general solution for the above case, where words can
        differ in length
        P.S I didn't read the same length query ;> and designed a full fledged function
        But then, came to know that all words have same length
    """
    n = len(s)
    chrs = sum([len(i) for i in words])
    if chrs > n:
        return []
    ans = []
    print(Counter(words))
    for i in range(n-chrs+1):
        prefix = [i-1]
        counter = Counter(words)
        enc = 0
        wc = len(counter)
        for j in range(i, i+chrs):
            for k in prefix:
                if s[k+1: j+1] in counter:
                    if prefix[-1] != j:
                        prefix.append(j)
                    counter[s[k+1:j+1]] -= 1
                    if counter[s[k+1:j+1]] == 0:
                        enc += 1
            if j == (i+chrs-1) and prefix[-1] == j:
                if enc == wc:
                    ans.append(i)
    return ans


def findSubstring(s: str, words):
    counter = Counter(words)
    w_len = len(words[0])
    num_words = len(words)
    n = len(s)
    ans = []

    for i in range(n-w_len*num_words+1):
        seen = dict()
        j = 0
        while j < num_words:
            word = s[i+j*w_len:i+(j+1)*w_len]
            if word in counter:
                seen.setdefault(word, 0)
                seen[word] += 1
                if seen[word] > counter[word]:
                    break
            else:
                break
            j += 1
        if j == num_words:
            ans.append(i)
    return ans


print(findSubstring("wordgoodgoodgoodbestword",
      ["word", "good", "best", "word"]))
