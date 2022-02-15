from collections import defaultdict

# Returns true if two trees are equal
def equalTree(node1, node2):
    if node1==None and node2==None:
        return True
    if node1==None or node2==None:
        return False
    if node1.data == node2.data:
        return equalTree(node1.left, node2.left)\
            and equalTree(node1.right, node2.right)
    else:
        return True
    
def preOrder(node, mp):
    if node:
        mp[node.data].append(node)
        preOrder(node.left, mp)
        preOrder(node.right, mp)
                    
def printAllDups(root):
    #code here
    mp = defaultdict(list)
    preOrder(root, mp)
    duplicates = set()

    for node in mp:
        # If more than one node is present, check for duplicate
        # tree among all other nodes with same data
        if len(mp[node]) > 1:
            temp = mp[node] 
            for i in range(len(temp)):
                for j in range(i+1, len(temp)):
                    if equalTree(temp[i], temp[j]):
                        duplicates.add(temp[i].data)
                        
    if duplicates:
        duplicates = list(duplicates)
        duplicates.sort()
        for j in duplicates:
            print(j, end=' ')
    else:
        print(-1, end=' ')