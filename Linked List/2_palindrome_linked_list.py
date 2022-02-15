def reverse(node, pre, end):
    if not node:
        return None
    prev = pre
    temp = node
    save = node
    while temp!=end:
        save = save.next
        temp.next = prev
        prev = temp
        temp = save
    return prev
    
def isPalindrome(head):
    if not head:
        return 0
    if not head.next:
        return 1
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow
    last = reverse(slow.next, slow, None)
    left = head
    right = last
    palindrome = True
    
    while right != middle:
        if right.data != left.data:
            palindrome = False
            break
        right = right.next
        left = left.next
        
    middle.next = reverse(last, None, middle)
    return int(palindrome)