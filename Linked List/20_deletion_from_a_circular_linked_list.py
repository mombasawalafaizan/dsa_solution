def deleteNode(head, key):
    if (head == None or (head.next==head and head.data==key) ):
        return None 

    #  Find the required node 
    curr = head.next
    prev = head 
    while True:
        if(curr==head):
            if(curr.data==key):
                prev.next = curr.next
                head = curr.next
            break
        if(curr.data==key):
            prev.next=curr.next
            break
        prev = curr
        curr=curr.next
    return head
        