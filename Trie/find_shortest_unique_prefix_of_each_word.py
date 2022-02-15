class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.freq = 0
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, x):
        return ord(x) - ord("a")

    def insert(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            idx = self._charToIndex(key[level])
            if not pCrawl.children[idx]:
                pCrawl.children[idx] = self.getNode()
            pCrawl.children[idx].freq += 1
            pCrawl = pCrawl.children[idx]
        pCrawl.isEndOfWord = True

    def getUniquePrefix(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            idx = self._charToIndex(key[level])
            pCrawl = pCrawl.children[idx]
            if pCrawl.freq == 1:
                return key[:level+1]
        return key

if __name__ == "__main__":
    arr = ["geeksgeeks", "geeksquiz", "geeksforgeeks", "zeb", "ze", "zenda", "zendor", "zendate", "zebra"]
    n = len(arr)
    trie = Trie()
    for i in range(n):
        trie.insert(arr[i])
    for i in arr:
        print(i,"->",trie.getUniquePrefix(i))