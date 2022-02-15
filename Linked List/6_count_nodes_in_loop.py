def countNodesinLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            i = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                i += 1
            return i
    return 0