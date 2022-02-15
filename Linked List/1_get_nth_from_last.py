def getNthfromEnd(head,n):
    #code here
    i = 0
    ahead = head
    while i<n-1 and ahead:
        ahead = ahead.next
        i+=1
    if ahead:
        behind = head
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        return behind.data
    else:
        return -1