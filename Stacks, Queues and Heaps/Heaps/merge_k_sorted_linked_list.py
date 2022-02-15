def heapify(heap, i, n):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and heap[l].data < heap[i].data:
        smallest = l
    if r < n and heap[r].data < heap[smallest].data:
        smallest = r
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(heap, smallest, n)

def heappop(heap, N):
    cur_smallest = heap[0]
    if heap[0].next == None:
        heap[0] = Node(float('inf'))
    else:
        heap[0] = heap[0].next
    heapify(heap, 0, N)
    return cur_smallest

def mergeKLists(heap,N):
    root = None
    prev = None
    for i in range(N//2-1, -1, -1):
        heapify(heap, i, N)
    while heap[0].data!=float('inf'):
        if root==None:
            root = heappop(heap, N)
            prev = root
        else:
            prev.next = heappop(heap, N)
            prev = prev.next
    return root

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None