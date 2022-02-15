from collections import deque, defaultdict

# Using DFS type approach
def topoSortUtil(v, visited, stack, graph):
    visited[v] = True
    for adj in graph[v]:
        if visited[adj] == False:
            topoSortUtil(adj, visited, stack, graph)
    stack.appendleft(v) # This is the only additional line than DFS algorithm
    
def topoSort(n, adj):
    visited = [False] * n
    stack = deque()
    for i in range(n):
        if visited[i]==False:
            topoSortUtil(i, visited, stack, adj)
    return stack


'''
dict : array of strings denoting the words in alien langauge
N : Size of the dictionary
K : Number of characters
'''
def findOrder(dict, N, K):
    # code here
    # return the string containing all k characters in correct order
    graph = defaultdict(list)
    for i in range(N-1):
        word1 = dict[i]
        word2 = dict[i+1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                graph[ord(word1[j])-97].append(ord(word2[j])-97)
                break
    alphabets = topoSort(K, graph)
    return [chr(97+i) for i in alphabets]