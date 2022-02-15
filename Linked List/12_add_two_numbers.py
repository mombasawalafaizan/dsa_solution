def reverse(head):
    cur = head
    save = head
    prev = None
    while cur:
        save = cur.next
        cur.next = prev
        prev = cur
        cur = save
    return prev

def addLists(first, second):
    new_first = reverse(first)
    new_second = reverse(second)
    prev = None
    carry = 0
    ans = LinkedList()
    while new_first and new_second:
        ans.insert((new_first.data + new_second.data + carry)%10)
        carry = (new_first.data + new_second.data + carry)//10
        new_first = new_first.next
        new_second = new_second.next
    while new_first:
        ans.insert((new_first.data + carry)%10)
        carry = (new_first.data + carry)//10
        new_first = new_first.next
    while new_second:
        ans.insert((new_second.data + carry)%10)
        carry = (new_second.data + carry)//10
        new_second = new_second.next
    if carry:
        ans.insert(carry)
    return reverse(ans.head)

'''No need to reverse lists given from geeks for geeks'''
# Following are the steps.
# 1) Calculate sizes of given two linked lists.
# 2) If sizes are same, then calculate sum using recursion. 
#    Hold all nodes in recursion call stack till the rightmost node, calculate the sum of 
#    rightmost nodes and forward carry to the left side.
# 3) If size is not same, then follow below steps:
# ….a) Calculate difference of sizes of two linked lists. Let the difference be diff
# ….b) Move diff nodes ahead in the bigger linked list. Now use step 2 to calculate the sum 
#      of the smaller list and right sub-list (of the same size) of a larger list. Also, store
#      the carry of this sum.
# ….c) Calculate the sum of the carry (calculated in the previous step) with the remaining left 
#      sub-list of a larger list. Nodes of this sum are added at the beginning of the sum list obtained the previous step.

# LINK OF THE ABOVE IMPLEMENTATION: https://www.geeksforgeeks.org/sum-of-two-linked-lists/