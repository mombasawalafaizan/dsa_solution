# Traverse the doubly linked list from left to right. For each current node during the traversal, initailze two 
# pointers first = pointer to the node next to the current node and last = pointer to the last node of the list. 
# Now, count pairs in the list from first to last pointer that sum up to value (x – current node’s data). 
# Add this count to the total_count of triplets. Pointer to the last node can be found only once in the beginning.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.last = None
    
    def append(self, val):
        nnode = Node(val)
        if not self.head:
            self.head = nnode
            self.last = nnode
        self.last.next = nnode
        nnode.prev = self.last
        self.last = nnode

    def countPairs(self, left, right, x):
    
        count = 0
        while left != right and left!=None and right!=None:
            if (left.data+right.data)==x:
                count += 1
                left = left.next
                if left == right:
                    break
                right = right.prev
            elif (left.data+right.data)>x:
                right = right.prev
            else:
                left = left.next
        return count

    def countTriplets(self, x):
        if self.head == None:
            return 0
        count = 0
        cur = self.head
        while cur:
            left= cur.next
            count+=self.countPairs(left, self.last, x - cur.data)
            cur = cur.next
        return count


    def __str__(self):
        temp = self.head
        s = 'NULL <- '
        while temp:
            s += str(temp.data) + " <=> "
            temp = temp.next
        if not s:
            return ''
        return s[:-4] + "-> NULL"

if __name__ == "__main__":
    dll = DLL()
    dll.append(1)
    dll.append(2)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(8)
    dll.append(9)
    print(dll)
    print(dll.countTriplets(17))