MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
def reverse(head):
    save = head
    temp = head
    prev = None
    while temp:
        save = temp.next
        temp.next = prev
        prev = temp
        temp = save
    return prev

def getSize(head):
    i = 0
    while head:
        head = head.next
        i+=1
    return i

def addLinkedList(a, b):
    carry = 0
    root = None
    last = None
    first = a
    second = b
    while first or second:
        fdata = first.data if first!=None else 0
        sdata = second.data if second!= None else 0
        res = (fdata + sdata + carry) % 10
        carry = (fdata + sdata + carry) // 10
        nnode = node()
        nnode.data = res
        if not root:
            root = nnode
        else:
            last.next = nnode
        last = nnode
        if first:
            first = first.next
        if second:
            second = second.next
    if carry>0:
        last.next = node()
        last.next.data = carry
    return root

def multiplyOneDigit(a, b: int):
    carry = 0
    root = None
    last = None
    first = a
    sdata = b
    while first:
        fdata = first.data
        res = (fdata * sdata + carry) % 10
        carry = (fdata * sdata + carry) // 10
        nnode = node()
        nnode.data = res
        if not root:
            root = nnode
        else:
            last.next = nnode
        last = nnode
        first = first.next
    if carry>0:
        last.next = node()
        last.next.data = carry
    return root

def multiplyTwoList(head1, head2):
    # Code here
    s1 = getSize(head1)
    s2 = getSize(head2)
    if s1 < s2:
        head1, head2 = head2, head1
    head1 = reverse(head1)
    head3 = None
    prev = None
    while head2:
        cur_digit = head2.data
        nnode = node()
        nnode.data = 0
        nnode.next = prev
        prev = nnode
        head3 = addLinkedList(prev, multiplyOneDigit(head1, cur_digit))
        prev = head3
        head2 = head2.next
    return reverse(head3)



#{ 
#  Driver Code Starts
class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        # printlist(list1.get_head())
        # print ''
        list2 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list2.insert(i)
        # printlist(list2.get_head())
        # print ''
        res = multiplyTwoList(list1.get_head(), list2.get_head())
        while res:
            print(res.data, end='')
            res = res.next
        print()
        