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

    def append(self, data):
        node = LinkedList.createNewNode(data)
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

def printList(head):
        temp = head
        s = ''
        while temp:
            s += str(temp.data) + " -> "
            temp = temp.next
        if not s:
            print('')
        print(s + "NULL")

def sortedMerge(a, b):
    result=None
    if a==None:
        return b
    if b==None:
        return a
    if a.data<=b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return result

def mergeSort(head):
    if head==None or head.next==None:
        return head
    middleNode = middleOfList(head)
    nextToMiddle = middleNode.next
    middleNode.next = None
    left = mergeSort(head)
    right = mergeSort(nextToMiddle)
    sortedList = sortedMerge(left, right)
    return sortedList
    
def middleOfList(head):
    if head == None:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    mylist = LinkedList()
    mylist.append(4)
    mylist.append(2)
    mylist.append(1)
    mylist.append(3)
    mylist.append(5)
    mylist.append(2)
    print(mylist)
    mylist.head = mergeSort(mylist.head)
    print(mylist)