class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
        self.mid = None
        self.size = 0

    def push(self, data):
        nnode = Node(data)
        if self.top != None:
            self.top.next = nnode
            nnode.prev = self.top
        if self.top == None:
            self.mid = nnode
        self.top = nnode
        if (self.size + 1)%2==0:
            self.mid = self.mid.next
        self.size += 1

    def pop(self):
        if self.top == None:
            return None
        data = self.top.data
        if (self.size-1)%2!=0:
            self.mid = self.mid.prev
        self.top = self.top.prev
        if self.top == None:
            self.mid = None
        if self.top:
            self.top.next = None
        self.size -= 1
        return data

    def findMiddle(self):
        if self.mid:
            return self.mid.data
        else:
            return None

    def deleteMiddle(self):
        if self.top==None or self.top.prev == None:
            self.top = None
            self.mid = None
            self.size = 0
            return None
        prev_mid = self.mid.prev
        next_mid = self.mid.next
        mid_data = self.mid.data
        prev_mid.next = next_mid
        if next_mid != None:
            next_mid.prev = prev_mid
        self.size -= 1
        if self.size%2==0:
            self.mid = next_mid
        else:
            self.mid = prev_mid
        if next_mid == None:
            self.top = self.mid
        return mid_data
    
    def __str__(self):
        stack = ''
        top = self.top
        while top:
            if top == self.top:
                stack += str(top.data)+" <- TOP\n"
            elif top == self.mid:
                stack += str(top.data)+" <- MID\n"
            else:
                stack += str(top.data)+"\n"
            top = top.prev
        return stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(32)
    stack.push(44)
    stack.push(41)
    print("Middle element: ", stack.findMiddle())
    print("Size: ", stack.size)
    print(stack)
    stack.pop()
    print("Middle element: ", stack.findMiddle())
    print("Size: ", stack.size)
    print(stack)
    stack.deleteMiddle()
    stack.deleteMiddle()
    # stack.deleteMiddle()
    print("Middle element: ", stack.findMiddle())
    print("Size: ", stack.size)
    print(stack)