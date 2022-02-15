class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.ll = []
        self.isEndOfWord = False

class Trie: 
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self): 
        return TrieNode() 

    def _charToIndex(self,ch): 
        return ord(ch)-ord('a') 


    def insert(self, key, i): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
        pCrawl.ll.append(i)
        pCrawl.isEndOfWord = True

def printAnagramsUtil(root, arr):
    if root==None: return
    if root.isEndOfWord:
        for idx in root.ll:
            print(arr[idx], end=' ')
    for i in range(26):
        if root.children[i]!=None:
            printAnagramsUtil(root.children[i], arr)

def printAnagramsTogether(arr, n):
    trie = Trie()
    for i in range(n):
        buffer = list(arr[i])
        buffer.sort()
        trie.insert(buffer, i)
    printAnagramsUtil(trie.root, arr)

if __name__ == '__main__':
    wordArr = ["cat", "dog", "tac", "god", "act", "gdo"]
    size = len(wordArr)
    printAnagramsTogether(wordArr, size)