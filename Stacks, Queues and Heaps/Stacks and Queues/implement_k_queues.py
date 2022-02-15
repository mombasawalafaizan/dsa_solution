class KQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * self.n
        self.rear = [-1] * self.k
        self.front = [-1] * self.k
        self.free = 0
        self.next = list(range(1, n))
        self.next.append(-1)
    
    def isEmpty(self, qn):
        return self.front[qn]==-1
    
    def isFull(self):
        return self.free == -1

    def enqueue(self, item, qn):
        if self.isFull():
            print('No free space available')
            return
        insert_at = self.free
        self.free = self.next[self.free]
        if self.isEmpty(qn):
            self.front[qn] = self.rear[qn] = self.free
        else:
            self.next[self.rear[qn]] = insert_at
            self.rear[qn] = insert_at
        self.next[insert_at] = -1
        self.arr[insert_at] = item

    def dequeue(self, qn):
        if self.isEmpty(qn):
            return None
        front_idx = self.front[qn]
        self.front[qn] = self.next[front_idx]
        self.next[front_idx] = self.free
        self.free = front_idx
        return self.arr[front_idx]

    def __str__(self):
        return 'arr: '+str(self.arr)+"\nfree: " + str(self.free) +"\nnext: "+ str(self.next) +"\nrear: "+ str(self.rear) + '\n'

if __name__ == "__main__":
    queue = KQueues(7, 2)
    print(queue)
    queue.enqueue(2, 0)
    queue.enqueue(5, 0)
    queue.enqueue(6, 0)
    # queue.enqueue(31, 1)
    # queue.enqueue(83, 1)
    print(queue)
    print(queue.dequeue(1))
    print(queue.dequeue(1))
    print(queue.dequeue(1))
    print(queue)
    queue.enqueue(99, 0)
    queue.enqueue(192, 0)
    queue.enqueue(299, 0)
    queue.enqueue(300, 0)
    queue.enqueue(322, 0)
    print(queue)