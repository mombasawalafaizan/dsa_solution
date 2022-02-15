def countNodes(head): 
  
    temp = head 
    result = 0
    if (head != None) : 
        while True : 
            temp = temp.next
            result = result + 1
            if (temp == head): 
                break
      
    return result 