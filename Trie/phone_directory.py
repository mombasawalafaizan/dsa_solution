# Given a list of contacts which exist in a phone directory and a query string str. 
# The task is to implement search query for the phone directory. Run a search query 
# for each prefix p of the query string str(i.e from  index 1 to str length) that prints
# all the distinct recommended contacts which have the same prefix as our query (p) in 
# lexicographical order.

class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False

class Trie: 
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self): 
        return TrieNode() 

    def _charToIndex(self,ch): 
        return ord(ch)-ord('a') 

    def insert(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
        pCrawl.isEndOfWord = True
        
    def searchNode(self, key):
        '''
        Used to find if the prefix is in TRIE or not
        If found, return the node else None
        '''
        pCrawl = self.root
        for level in range(len(key)):
            index =  self._charToIndex(key[level])
            if pCrawl.children[index] == None:
                return None
            pCrawl = pCrawl.children[index]
        return pCrawl

def printMatches(node, strr):
    '''
    Used to print the matches for all the prefixes
    '''
    if node.isEndOfWord:
        print(strr, end=' ')
    for i in range(26):
        if node.children[i]:
            printMatches(node.children[i], strr+chr(97+i))

def printAns(directory, query):
    trie = Trie()
    for word in directory:
        trie.insert(word)
    for i in range(1, len(query)+1):
        startNode = trie.searchNode(query[:i])
        # No such prefix found
        if startNode == None: 
            print(0)
        else:
            printMatches(startNode, query[:i]) # Prefix in the string will already be there
            print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        directory = input().split()
        query = input()
        printAns(directory, query)