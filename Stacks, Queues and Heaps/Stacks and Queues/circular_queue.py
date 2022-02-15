class CircularQueue:
    def __init__(self, n):
        self.arr = [0] * n
        self.n = n
        self.front = -1
        self.rear = -1

    def enqueue(self, el):
        if (self.rear+1)%self.n == self.front:
            print('Queue is full')
            return
        self.rear = (self.rear+1)%self.n
        self.arr[self.rear] = el
        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.front == -1:
            print('Empty queue')
            return None
        x = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1)%self.n
        return x

    def display(self): 
      
        # condition for empty queue 
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.arr[i], end = " ") 
            print () 
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.n): 
                print(self.arr[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.arr[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.n == self.front): 
            print("Queue is Full") 

ob = CircularQueue(5) 
ob.enqueue(14) 
ob.enqueue(22) 
ob.enqueue(13) 
ob.enqueue(-6) 
ob.display() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.display() 
ob.enqueue(9) 
ob.enqueue(20) 
ob.enqueue(5) 
ob.display()