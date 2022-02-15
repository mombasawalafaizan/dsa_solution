def removeDuplicates(head):
    if head:
        traversed = set()
        traversed.add(head.data)
        prev = head
        temp = head.next
    else:
        temp = None
    while temp:
        if temp.data in traversed:
            temp = temp.next
        else:
            traversed.add(temp.data)
            prev.next = temp
            prev = temp
            temp = temp.next
    prev.next = temp
    return head