from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i] + '_' + word[i+1:]].append(word)
        visited = set()
        q = deque([(beginWord, 1)])
        while q:
            word, k = q.popleft()
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    neighbors = word[:i] + '_' + word[i+1:]
                    for neighbor in adj[neighbors]:
                        if neighbor not in visited:
                            if neighbor == endWord:
                                return k+1
                            q.append((neighbor, k+1))
        return 0