def findMid(head):
    '''Finds the middle of the linked list'''
    # For odd elements middle is found nicely
    # For even elements middle is n/2th element
    # if implemented like this
    # eg. if 6 elements middle is 4th element
    # but if,
    # while fast.next and fast.next.next is used
    # middle is 3rd element
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data