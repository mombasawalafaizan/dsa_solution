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

    def findPairs(self, x):
        left = self.head
        right = self.last
        pairs = []
        while left != right and left!=None and right!=None:
            if (left.data+right.data)==x:
                pairs.append([left.data, right.data])
                left = left.next
                if left == right:
                    break
                right = right.prev
            elif (left.data+right.data)>x:
                right = right.prev
            else:
                left = left.next
        return pairs


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
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(8)
    dll.append(9)
    print(dll)
    print(dll.findPairs(7))