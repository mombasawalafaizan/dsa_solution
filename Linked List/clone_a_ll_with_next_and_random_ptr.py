class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb = None


# O(n) time and O(n) space solution
def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    if not head:
        return None
    temp = head
    copy_head = None
    last = None
    store = [] # This will aquire more n space
    while temp:
        store.append(temp)
        nnode = Node(temp.data)
        temp1 = temp
        temp = temp.next
        temp1.next = nnode
        nnode.arb = temp1
        if last==None:
            copy_head = nnode
        else:
            last.next = nnode
        last = nnode
    last.next = None

    cnode = copy_head
    while cnode:
        if cnode.arb.arb:
            cnode.arb = cnode.arb.arb.next
        else:
            cnode.arb = None
        cnode = cnode.next
        
    for i in range(len(store)-1):
        store[i].next = store[i+1]
    store[len(store)-1].next = None
        
    return copy_head

# O(n) time and O(1) space solution
def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    if not head:
        return None
    original_node = head
    while original_node:
        cnode = Node(original_node.data)
        cnode.next = original_node.next
        temp = original_node.next
        original_node.next = cnode
        original_node = temp
    
    original_node = head    
    while original_node:
        if original_node.arb:
            original_node.next.arb = original_node.arb.next
        original_node = original_node.next.next
    
    original_node = head
    copy_head = head.next
    cnode = head.next
    while True:
        original_node.next = original_node.next.next
        if cnode.next != None:
            cnode.next = cnode.next.next
        else:
            break
        original_node = original_node.next
        cnode = cnode.next
    original_node.next =None
    
    return copy_head