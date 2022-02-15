class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.last = None
    
    def append(self, val):
        nnode = Node(val)
        if not self.head:
            self.head = nnode
            self.last = nnode
        self.last.next = nnode
        nnode.prev = self.last
        self.last = nnode
    
    def reverse(self):
        #return head after reversing
        previous = None
        cur = self.head
        save = self.head
        while cur:
            save = cur.next
            cur.next =  previous
            cur.prev = save
            previous = cur
            cur = save
        self.head = previous