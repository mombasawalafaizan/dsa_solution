def findWinner(x, y, n): 
      
    # To store results 
    dp = [0 for i in range(n + 1)] 
  
    # Initial values 
    dp[0] = False
    dp[1] = True
  
    # Computing other values. 
    for i in range(2, n + 1): 
  
        # If A losses any of i-1 or i-x 
        # or i-y game then he will 
        # definitely win game i 
        if (not dp[i - 1]): 
            dp[i] = True
        elif (i - x >= 0 and not dp[i - x]): 
            dp[i] = True
        elif (i - y >= 0 and not dp[i - y]): 
            dp[i] = True
  
        # Else A loses game. 
        else: 
            dp[i] = False
  
    # If dp[n] is true then A will 
    # game otherwise he losses 
    return dp[n] 