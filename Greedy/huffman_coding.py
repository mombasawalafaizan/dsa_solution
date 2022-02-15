from heapq import heapify, heapreplace, heappop
from collections import deque

class TreeNode:
    def __init__(self, data,  char=None):
        self.data = data
        self.left = None
        self.right = None
        self.char = char
        
    def __gt__(self, other):
        '''Function to compare treenodes in heap'''
        return self.data > other.data    
            
def printHuffmanCodes(root, curCode):
    if not root:
        return
    if not root.left and not root.right:
        print(curCode, end=' ')
        return
    if root.left:
        printHuffmanCodes(root.left, curCode+"0")
    if root.right:
        printHuffmanCodes(root.right, curCode+"1")        
        
def createMergeTree(heap, n):
    for _ in range(n-1):
        nnode = TreeNode(0)
        nnode.left = heappop(heap)
        nnode.right = heap[0]
        nnode.data = nnode.left.data + heap[0].data
        heapreplace(heap, nnode)
    return heap[0]
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        alphas = list(input())
        freqs = list(map(int, input().split()))
        n = len(freqs)
        heap = [TreeNode(freqs[i], alphas[i]) for i in range(n)]
        heapify(heap)
        root = createMergeTree(heap, n)
        printHuffmanCodes(root, '')
        print()