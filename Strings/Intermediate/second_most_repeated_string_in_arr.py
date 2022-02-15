from collections import Counter
def secFrequent(arr, n):
        freq = Counter(arr)
        first = float('-inf')
        second = float('-inf')
        for i in freq.values():
            if i > first:
                second = first
                first = i
            elif i > second:
                second = i
        
        for i in freq:
            if freq[i]==second:
                return i
        return -1