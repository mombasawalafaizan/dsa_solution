def deleteList(self): 
          
        # initialize the current node 
        current = self.head 
        while current: 
            prev = current.next # move next node 
              
            # delete the current node 
            del current.data 
              
            # set current equals prev node 
            current = prev