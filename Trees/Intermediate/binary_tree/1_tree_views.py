from collections import deque

def topView(root):
    if not root:
        return
    mydict = {}
    q = deque()
    q.append([root, 0])
    while q:
        cur_node, cur_level = q.popleft()
        if cur_level not in mydict:
            mydict[cur_level] = cur_node.data
        if cur_node.left:
            q.append([cur_node.left, cur_level - 1])
        if cur_node.right:
            q.append([cur_node.right, cur_level + 1])
            
    for i in sorted(mydict):
        print(mydict[i], end=' ')

def bottomView(root):
    if not root:
        return
    mydict = {}
    q = deque()
    q.append([root, 0])
    while q:
        cur_node, cur_level = q.popleft()
        mydict[cur_level] = cur_node.data
        if cur_node.left:
            q.append([cur_node.left, cur_level - 1])
        if cur_node.right:
            q.append([cur_node.right, cur_level + 1])
            
    for i in sorted(mydict):
        print(mydict[i], end=' ')

        
def LeftView(root):
    def helper(root, level, store):
        if root:
            if level > len(store)-1:
                store.append(root.data)
            helper(root.left, level+1, store)
            helper(root.right, level+1, store)

    store = []            
    helper(root, 0, store)
    return store

    # # If we just have to print the data, then better solution
    # def helper(root, level, store):
    #     if root:
    #         if level > store[0]:
    #             print(root.data, end=' ')
    #             store[0] = level
    #         helper(root.left, level+1, store)
    #         helper(root.right, level+1, store)
  
    # helper(root, 0, [-1])
    

def RightView(root):
    def helper(root, level, store):
        if root:
            if level > len(store)-1:
                store.append(root.data)
            helper(root.right, level+1, store)
            helper(root.left, level+1, store)

    store = []            
    helper(root, 0, store)
    return store