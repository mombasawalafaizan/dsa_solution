from heapq import _heapify_max, _heappop_max
import math
class Solution:
    class HeapNode:
        def __init__(self, char, frequency):
            self.char = char
            self.frequency = frequency
        def __lt__(self, other):
            return self.frequency < other.frequency
        
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''
        letters = [0] * 26
        for ch in S:
            letters[ord(ch)-97]+=1
        heap = []
        for i in range(26):
            if letters[i] > 0:
                heap.append(self.HeapNode(chr(97+i), letters[i]))
        _heapify_max(heap)
        n = len(S)
        l = len(heap)
        ans=[' '] * n
        i = 0
        while l != 0:
            cur = _heappop_max(heap)
            if cur.frequency > math.ceil(n/2):
                return ''
            reduce = cur.frequency
            while reduce != 0:
                if ans[i] != ' ':
                    i += 1
                ans[i] = cur.char
                i = (i+2)%n
                reduce -= 1
            l -= 1
        return ''.join(ans)