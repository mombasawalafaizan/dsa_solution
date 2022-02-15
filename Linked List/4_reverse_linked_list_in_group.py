class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, node: Node):
        if self.head:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = node
        else:
            self.head = node
        self.size += 1

    def __str__(self):
        temp = self.head
        s = ''
        while temp:
            s += str(temp.data) + " -> "
            temp = temp.next
        if not s:
            return ''
        return s + "NULL"

    # Iterative implementation
    def reverse(self, k=3):
        temp = self.head
        store_last = temp
        store_old = None
        prev = None
        root = None
        i = 1
        while temp:
            save = temp.next
            temp.next = prev
            prev = temp
            temp = save
            if i%k==0:
                if root == None:
                    root = prev
                if store_old!=None:
                    store_old.next = prev
                store_old = store_last
                store_last = temp
                prev = None
            i += 1
        if store_old:
            store_old.next = prev
        else:
            root = prev
        self.head=root

    # Recursive implementation
    def reverse(self, head, k): 
        current = head  
        next  = None
        prev = None
        count = 0 
          
        # Reverse first k nodes of the linked list 
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next 
            count += 1
  
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverse(next, k) 
  
        # prev is new head of the input list 
        return prev
    
if __name__ == "__main__":
    ll= LinkedList()
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    ll.append(Node(4))
    print(ll)
    ll.reverse()
    print(ll)