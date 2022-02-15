# Similar to question 4, just add prev link

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

    def __str__(self):
        temp = self.head
        s = 'NULL <- '
        while temp:
            s += str(temp.data) + " <=> "
            temp = temp.next
        if not s:
            return ''
        return s[:-4] + "-> NULL"


def reverse(node, k):
    cur = node
    save = node
    prev = None
    i = 0
    while i<k and cur:
        save = cur.next
        cur.next = prev
        cur.prev = save
        prev = cur
        cur = save
        i+=1
    
    if cur:
        first_in_group = reverse(cur, k)
        node.next = first_in_group
        first_in_group.prev = node
        # node.next = reverse(cur, k)
        # node.next.prev = node

    return prev


if __name__ == "__main__":
    dll = DLL()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(7)
    dll.append(8)
    print(dll)
    dll.head = reverse(dll.head, 3)
    print(dll)