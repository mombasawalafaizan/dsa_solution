# Returns maximum profit with two transactions on a given  
# list of stock prices price[0..n-1] 
def maxProfit(price,n): 
    # Create profit array and initialize it as 0 
    profit = [0]*n 
      
    # Get the maximum profit with only one transaction 
    # allowed. After this loop, profit[i] contains maximum 
    # profit from price[i..n-1] using at most one trans. 
    max_price=price[n-1] 
      
    for i in range( n-2, -1 ,-1): 
          
        if price[i]> max_price: 
            max_price = price[i] 
              
        # we can get profit[i] by taking maximum of: 
        # a) previous maximum, i.e., profit[i+1] 
        # b) profit by buying at price[i] and selling at 
        #    max_price 
        profit[i] = max(profit[i+1], max_price - price[i]) 
          
    print('Profit array after one transaction:', profit)
    # Get the maximum profit with two transactions allowed 
    # After this loop, profit[n-1] contains the result     
    min_price=price[0] 
      
    for i in range(1,n): 
          
        if price[i] < min_price: 
            min_price = price[i] 
  
        # Maximum profit is maximum of: 
        # a) previous maximum, i.e., profit[i-1] 
        # b) (Buy, Sell) at (min_price, A[i]) and add 
        #    profit of other trans. stored in profit[i]     
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price)) 
    print('Profit array after two transactions:', profit)
    result = profit[n-1] 
      
    return result 
if __name__ == '__main__':
    #price = [2, 30, 15, 10, 8, 25, 80] 
    price = [100, 30, 15, 10, 8, 25, 80]
    print(price)
    #price = list(map(int, input().split()))
    print("Maximum profit is", maxProfit(price, len(price)))