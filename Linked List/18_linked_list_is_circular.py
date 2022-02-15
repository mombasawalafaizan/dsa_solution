def isCircular(head):
    # Code here
    if not head:
        return 0
    cur = head
    while True:
        if cur.next==None:
            return 0
        elif cur.next==head:
            return 1
        else:
            cur = cur.next