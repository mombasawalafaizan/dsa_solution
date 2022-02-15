def intersetPoint(head_a,head_b):
    last_a = None
    last_b = None
    ptr_a = head_a
    ptr_b = head_b
    while ptr_a != ptr_b:
        if ptr_a.next == None:
            if not last_a:
                last_a = ptr_a
                ptr_a = head_b
        if ptr_b.next == None:
            if not last_b:
                last_b = ptr_b
                ptr_b = head_a
        if (last_a and last_b) and last_a != last_b:
            return -1
        ptr_a = ptr_a.next
        ptr_b = ptr_b.next
    return ptr_a.data

'''Another method:
USING difference OF NODE COUNTS d = abs(c1-c2)   O(m+n) time complexity'''
# a) Get count of the nodes in the first list, let count be c1.
# b) Get count of the nodes in the second list, let count be c2.
# c) Get the difference of counts d = abs(c1 – c2)
# d) Now traverse the bigger list from the first node till d nodes 
#    so that from here onwards both the lists have equal no of nodes.
# e) Then we can traverse both the lists in parallel till we come across 
#    a common node. (Note that getting a common node is done by comparing the address of the nodes)