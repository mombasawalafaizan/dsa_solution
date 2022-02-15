# If you buy one item, you get k items free
# So, you have to determine minCost and maxCost
def shopCandy(price, n, k):
    price.sort()
    min_cost, max_cost, cur_free = 0, 0, 0
    for i in range(n):
        if i < (n-cur_free):
            min_cost += price[i]
        if (n-i-1) >= cur_free:
            max_cost += price[n-i-1]
        else: # For improving efficiency
            break
        cur_free += k
    return(min_cost, max_cost)

if __name__ == '__main__':
    arr = [3, 2, 1, 4]
    k = 2
    print(shopCandy(arr, len(arr), k))
    
            