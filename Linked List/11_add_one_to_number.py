class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    temp = head
    save = head
    prev = None
    while temp:
        save = temp.next
        temp.next = prev
        prev = temp
        temp = save
    return prev
    
def addOne(head):
    #Returns new head of linked List.
    reverse_digits = reverse(head)
    store = reverse_digits
    carry = 1
    prev = None
    while carry and reverse_digits:
        carry = (reverse_digits.data + 1) // 10
        reverse_digits.data = (reverse_digits.data + 1) % 10
        prev = reverse_digits
        reverse_digits = reverse_digits.next
    if carry:
        prev.next = Node(1)
    return reverse(store)


'''Recursive implementation without reversing the list'''
# Recursively add 1 from end to beginning and returns 
# carry after all nodes are processed. 
def addWithCarry(head): 
  
    # If linked list is empty, then 
    # return carry 
    if (head == None): 
        return 1
  
    # Add carry returned be next node call 
    res = head.data + addWithCarry(head.next) 
  
    # Update data and return new carry 
    head.data = int((res) % 10) 
    return int((res) / 10) 
  
# This function mainly uses addWithCarry(). 
def addOne(head): 
  
    # Add 1 to linked list from end to beginning 
    carry = addWithCarry(head) 
  
    # If there is carry after processing all nodes, 
    # then we need to add a new node to linked list 
    if (carry != 0): 
      
        newNode = Node(0) 
        newNode.data = carry 
        newNode.next = head 
        return newNode # New node becomes head now 
      
    return head