from collections import defaultdict
def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    
    #code here
    anagrams = defaultdict(list)
    for i in range(n):
        chars = [0] * 26
        for j in words[i]:
            chars[97-ord(j)]+=1
        anagram = ''
        for j in range(26):
            anagram += (chars[j] * chr(97+j))
        anagrams[anagram].append(words[i])
    return list(anagrams.values())
