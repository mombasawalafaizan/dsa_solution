from heapq import heapify, heapreplace

class HeapNode:
    def __init__(self, i, j, el):
        self.i = i
        self.j = j
        self.el = el
    
    def __lt__(self, other):
        return self.el < other.el

def smallestRange(numbers):
    k = len(numbers)
    n = len(numbers[0])
    minheap = [HeapNode(i, 0,numbers[i][0]) for i in range(k)]
    cur_max = max(minheap).el
    heapify(minheap)
    r = [minheap[0].el, cur_max]
    while True:
        smallest = minheap[0]
        if (cur_max-smallest.el)<(r[1]-r[0]):
            r = [smallest.el, cur_max]
        if (smallest.j + 1) == n:
            break
        next_node = HeapNode(smallest.i, smallest.j+1,\
        numbers[smallest.i][smallest.j+1])
        heapreplace(minheap, next_node)
        if next_node.el > cur_max:
            cur_max = next_node.el
    return r