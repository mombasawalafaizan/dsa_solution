
def findIntersection(head1,head2):
    #return head
    list3 = linkedList()
    while head1 and head2:
        if head1.data == head2.data:
            list3.insert(head1.data)
            head1 = head1.next
            head2 = head2.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            head1 = head1.next
    return list3.head