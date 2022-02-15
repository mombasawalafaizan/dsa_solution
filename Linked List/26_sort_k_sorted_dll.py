# Using heap we store the nodes in heap of size k and get minimum of nodes
# from the heap. Time complexity: O(n log k) and Auxillary space: O(k)
from heapq import heappush, heappop

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    # Used for comparison
    def __lt__(self, other):
        return self.data < other.data

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

    def sortAKSortedDLL(self, k):
        if not self.head:
            return self.head
        head = self.head
        last = None
        heap = []
        new_head = None
        for i in range(k+1):
            if head:
                heappush(heap, head)
                head = head.next
        while heap:
            if new_head==None:
                new_head = heappop(heap)
                new_head.prev = None
                last = new_head
            else:
                last.next = heap[0]
                heap[0].prev = last
                last = heappop(heap)
            if head!=None:
                heappush(heap, head)
                head = head.next
        last.next = None
        self.head = new_head

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
    dll.append(3)
    dll.append(6)
    dll.append(2)
    dll.append(12)
    dll.append(56)
    dll.append(8)
    print(dll)
    dll.sortAKSortedDLL(2)
    print(dll)