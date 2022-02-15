class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, key):
        pCrawl = self.root
        l = len(key)
        for i in range(l):
            idx = ord(key[i]) - 97
            if not pCrawl.children[idx]:
                pCrawl.children[idx] = self.getNode()
            pCrawl = pCrawl.children[idx]
        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        l = len(key)
        for i in range(l):
            idx = ord(key[i]) - 97
            if not pCrawl.children[idx]:
                return False
            pCrawl = pCrawl.children[idx]
        return pCrawl != None and pCrawl.isEndOfWord
