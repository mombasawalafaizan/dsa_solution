def moveToFront(self): 
        tmp = self.head 
        sec_last = None # To maintain the track of 
                        # the second last node 
  
    # To check whether we have not received  
    # the empty list or list with a single node 
        if not tmp or not tmp.next:  
            return
  
        # Iterate till the end to get 
        # the last and second last node  
        while tmp and tmp.next : 
            sec_last = tmp 
            tmp = tmp.next
  
        # point the next of the second 
        # last node to None 
        sec_last.next = None
  
        # Make the last node as the first Node 
        tmp.next = self.head 
        self.head = tmp