# Iterative version
def reverseList(head):
    temp = head
    prev = None
    while temp:
        save = temp.next
        temp.next = prev
        prev = temp
        temp = save
    return prev

# Recursive version
def reverse(head):
    if not head.next:
        return head.next
    newHead = reverse(head.next)
    head.next.next = head
    head.next = None
    return newHead