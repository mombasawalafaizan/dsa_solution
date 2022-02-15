class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    @staticmethod
    def createNewNode(data):
        return Node(data)

    def appendleft(self, node: Node):
        node.next = self.head
        self.head = node
        self.size += 1

    def append(self, node: Node):
        if self.head:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = node
        else:
            self.head = node
        self.size += 1

    def search(self, data):
        temp = self.head
        i = 0
        while temp:
            if temp.data == data:
                return i
            temp = temp.next
            i += 1
        return -1

    def remove(self, data):
        if not self.head:
            return False
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            self.size -= 1
            return True
        else:
            while temp.next and temp.next.data!=data:
                temp = temp.next
            if temp.next:
                temp.next = temp.next.next
                self.size -= 1
                return True
            else:
                return False
    
    def pop(self, idx):
        if not self.head:
            return None
        temp = self.head
        if idx == 0:
            self.head = self.head.next
            self.size -= 1
            return temp.data
        else:
            i = 0
            while temp.next and i<idx-1:
                temp = temp.next
                i+=1
            if i == self.size-1:
                return None
            else:
                data = temp.next.data
                temp.next = temp.next.next
                self.size -= 1
                return data

    def min(self):
        if self.head:
            temp = self.head
            minimum = temp.data
            while temp:
                if minimum > temp.data:
                    minimum = temp.data
                temp = temp.next
            return minimum
        else:
            return None

    def max(self):
        if self.head:
            temp = self.head
            maximum = temp.data
            while temp:
                if maximum < temp.data:
                    maximum = temp.data
                temp = temp.next
            return maximum
        else:
            return None
    
    def getNthfromEnd(self, n):
        '''Get Nth element from end'''
        i = 0
        ahead = head
        while i<n-1 and ahead:
            ahead = ahead.next
            i+=1
        if ahead:
            behind = head
            while ahead.next:
                ahead = ahead.next
                behind = behind.next
            return behind.data
        else:
            return -1

    def count(self, value):
        temp = self.head
        count = 0
        while temp:
            if temp.data == value:
                count += 1
            temp = temp.next
        return count

    def toCircular(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        self.last = temp
        self.last.next = self.head

    def deleteList(self): 
          
        # initialize the current node 
        current = self.head 
        while current: 
            prev = current.next # move next node 
              
            # delete the current node 
            del current.data 
              
            # set current equals prev node 
            current = prev
            
    def __len__(self):
        return self.size

    def __str__(self):
        temp = self.head
        s = ''
        while temp:
            s += str(temp.data) + " -> "
            temp = temp.next
        if not s:
            return ''
        return s + "NULL"




if __name__ == "__main__":
    opt = 1
    ll = LinkedList()
    while opt!=0:
        print('1: Add node at beginning')
        print('2: Add node at end')
        print('3: Length of linked list')
        print('4: Print linked list')
        print('5: Count occurrence of data in linked list')
        print('6: Maximum element in linked list')
        print('7: Minimum element in linked list')
        print('8: Remove an element from linked list(by inputting data)')
        print('9: Remove an element from linked list(by inputting index)')
        opt = int(input('\nEnter option(1-9)(0 to exit): '))
        print()
        if opt == 1:
            data = int(input('Enter data to enter in linked list: '))
            ll.appendleft(LinkedList.createNewNode(data))
        elif opt == 2:
            data = int(input('Enter data to enter in linked list: '))
            ll.append(LinkedList.createNewNode(data))
        elif opt==3:
            print('Length of the linked list: ',len(ll))
        elif opt == 4:
            print(ll)
        elif opt == 5:
            data = int(input('Enter data whose occurrence is to be found: '))
            print("Frequency: ",ll.count(data))
        elif opt == 6:
            print("Maximum element in linked list:", ll.max())
        elif opt == 7:
            print("Minimum element in linked list:", ll.min())
        elif opt == 8:
            data = int(input('Enter data to be removed from linked list: '))
            if ll.remove(data):
                print('Succesfully removed.')
            else:
                print('NOT FOUND') 
        elif opt == 9:
            idx = int(input('Enter index of element to be removed from linked list: '))
            data = ll.pop(idx)
            if data:
                print('Data at index',idx,'is',data)
            else:
                print('Invalid index entered.') 
        print()
