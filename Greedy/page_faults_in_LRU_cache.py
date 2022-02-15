from collections import OrderedDict

class LRU:
    def __init__(self, size):
        self.size = size
        self.lru = OrderedDict()
        
    def set(self, item):
        '''
        Set the item in LRU
        If item already in LRU, return True else False
        '''
        if item in self.lru:
            self.lru.move_to_end(item)
            return True
        if self.size == 0:
            self.lru.popitem(last=False)
        else:
            self.size -= 1
        self.lru[item] = 0
        return False
                

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        pages = list(map(int, input().split()))
        space = int(input())

        lru = LRU(space)
        faults = 0
        for page in pages:
            # If page not in lru, increment fault
            if lru.set(page)==False:
                faults += 1
        print(faults)