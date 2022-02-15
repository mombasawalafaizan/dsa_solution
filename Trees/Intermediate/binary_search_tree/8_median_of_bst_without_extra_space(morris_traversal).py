def countNodes(root):
    current = root
    count = 0
    while current!=None:
        if current.left == None:
            count+=1
            current = current.right
        else:
            pre = current.left
            while pre.right != None and pre.right!=current:
                pre = pre.right
            if pre.right==None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                count+=1
                current = current.right
    return count

def findMedian(root):
    if not root:
        return 0
    cnt = countNodes(root)
    currCount = 0
    current = root
    prev = root

    while current!=None:
        if current.left==None:
            currCount+=1
            if cnt%2!=0 and (cnt+1)//2 == currCount:
                return prev.data
            elif cnt%2==0 and currCount == (cnt//2)+1:
                return (prev.data + current.data)//2
            prev = current
            current = current.right
        else:
            pre = current.left
            while pre.right!=None and pre.right!=current:
                pre = pre.right
            if pre.right==None:
                pre.right=current
                current=current.left
            else:
                pre.right = None
                prev = pre
                currCount+=1
                if cnt%2!=0 and (cnt+1)//2 == currCount:
                    return prev.data
                elif cnt%2==0 and currCount == (cnt//2)+1:
                    return (prev.data + current.data)//2
                prev = current
                current = current.right