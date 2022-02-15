class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    

class DLL:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    
    def append(self, val):
        nnode = Node(val)
        if not self.head:
            self.head = nnode
            self.last = nnode
        self.last.next = nnode
        nnode.prev = self.last
        self.last = nnode
        self.size += 1

    def rotate(self, N=1):
        if N >= self.size:
            N = N % self.size
        if N==0:
            return
        head = self.head
        temp = self.head
        pos = 1
        # Go upto Nth node
        while pos<N:
            temp = temp.next
            pos+=1
        new_head = temp.next
        new_head.prev = None
        temp.next = None
        
        # Traverse to last node, to join the links
        head.prev = self.last
        self.last.next = head
        self.head = new_head
        self.last = temp
    
    def __str__(self):
        temp = self.head
        s = 'NULL <- '
        while temp:
            s += str(temp.data) + " <=> "
            temp = temp.next
        if not s:
            return ''
        return s[:-4] + "-> NULL"

if __name__ == "__main__":
    dll = DLL()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    print(dll)
    dll.rotate(2)
    print(dll)