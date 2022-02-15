class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def areAnagrams(root1, root2) : 
  
    # Base Cases  
    if (root1 == None and root2 == None) : 
        return True
    if (root1 == None or root2 == None) : 
        return False
  
    # start level order traversal of  
    # two trees using two queues.  
    q1 = [] 
    q2 = []  
    q1.append(root1)  
    q2.append(root2)  
  
    while (1) : 
      
        # n1 (queue size) indicates number  
        # of Nodes at current level in first 
        # tree and n2 indicates number of nodes 
        # in current level of second tree.  
        n1 = len(q1) 
        n2 = len(q2) 
  
        # If n1 and n2 are different  
        if (n1 != n2): 
            return False
  
        # If level order traversal is over  
        if (n1 == 0):  
            break
  
        # Dequeue all Nodes of current level  
        # and Enqueue all Nodes of next level 
        curr_level1 = [] 
        curr_level2 = [] 
        while (n1 > 0):  
            node1 = q1[0]  
            q1.pop(0)  
            if (node1.left != None) : 
                q1.append(node1.left)  
            if (node1.right != None) : 
                q1.append(node1.right)  
            n1 -= 1
  
            node2 = q2[0]  
            q2.pop(0)  
            if (node2.left != None) : 
                q2.append(node2.left)  
            if (node2.right != None) : 
                q2.append(node2.right)  
  
            curr_level1.append(node1.data)  
            curr_level2.append(node2.data)  
              
        # Check if nodes of current levels  
        # are anagrams or not.  
        curr_level1.sort()  
        curr_level2.sort()  
        if (curr_level1 != curr_level2) : 
            return False
      
    return True