def removeDuplicates(head):
    temp = head
    while temp:
        prev = temp
        temp = temp.next
        while temp and prev.data == temp.data:
            temp = temp.next
        prev.next = temp