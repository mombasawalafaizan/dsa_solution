from collections import deque
# This will take O(m+n) time and O(m+n) space complexity
def getInorder(root, ino):
    if root:
        getInorder(root.left, ino)
        ino.append(root.data)
        getInorder(root.right, ino)

def merge(root1, root2):
    #code here.
    bst1 = []
    getInorder(root1, bst1)
    bst2 = []
    getInorder(root2, bst2)
    i = 0
    j = 0
    ans = []
    while i<len(bst1) and j<len(bst2):
        if bst1[i] < bst2[j]:
            ans.append(bst1[i])
            i += 1
        else:
            ans.append(bst2[j])
            j += 1
    while i < len(bst1):
        ans.append(bst1[i])
        i += 1
    while j < len(bst2):
        ans.append(bst2[j])
        j += 1
    return ans


# This will take O(height1 + height2) time

def merge_less_space(root1, root2):
    #code here.
    stack1 = deque()
    stack2 = deque()
    ans = []
    cur1 = root1
    cur2 = root2
    while True:
        while cur1:
            stack1.append(cur1)
            cur1 = cur1.left
        while cur2:
            stack2.append(cur2)
            cur2 = cur2.left
        if stack1 or stack2:
            if ((stack1 and stack2) and (stack1[-1].data < stack2[-1].data)) or\
            (stack1 and not stack2):
                cur1 = stack1.pop()
                ans.append(cur1.data)
                cur1 = cur1.right
            else:
                cur2 = stack2.pop()
                ans.append(cur2.data)
                cur2 = cur2.right
        else:
            break
        
    return ans