class TrieNode: 
    def __init__(self): 
        self.children = [None]*2
        self.isEndOfWord = False

class Trie: 
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self): 
        return TrieNode() 

    def insert(self, row): 
        pCrawl = self.root 
        already_there = True
        for i in range(len(row)): 
            if not pCrawl.children[row[i]]: 
                pCrawl.children[row[i]] = self.getNode() 
                already_there = False
            pCrawl = pCrawl.children[row[i]] 
        pCrawl.isEndOfWord = True
        return already_there

def uniqueRow(row, col, matrix):
    #complete the function
    trie = Trie()
    res = []
    for i in range(row):
        if trie.insert(matrix[i]) == False:
            res.append(matrix[i])
    return res

matrix = [
    [0, 1, 0, 0, 1],  
    [1, 0, 1, 1, 0],  
    [0, 1, 0, 0, 1],  
    [1, 0, 1, 0, 0]
]
print(uniqueRow(len(matrix), len(matrix[0]), matrix))