def suvival(S, N, M):
    '''
    :param S: Number of days to suvive
    :param N: Maximum food man can buy on a day
    :param M: Required food for each day
    :O/P: Minimum number of days customer has to buy food from shop or -1 if not possible
    NOTE: Customer cannot buy food on Sundays(start computing from Monday)
    '''

    # GFG approach

    # If we can not buy at least a week  
    # supply of food during the first week 
    # OR We can not buy a day supply of food  
    # on the first day then we can't survive. 
    if (((N * 6) < (M * 7) and S > 6) or M > N):  
        print("No") 
    else: 
          
        # If we can survive then we can 
        # buy ceil(A / N) times where A is 
        # total units of food required. 
        days = (M * S) / N 
          
        if (((M * S) % N) != 0): 
            days += 1
        print("Yes "), 
        print(days) 

    # Faizan's approach
    # if N < M:
    #     print('No')
    #     return
    # days_passed = 0
    # buy = 0
    # while days_passed < S:
    #     days_passed += N // M
    #     if (days_passed + 1)%7==0:
    #         days_passed -= 1
    #     buy += 1
    # print('Yes', buy)

suvival(10, 20, 30)