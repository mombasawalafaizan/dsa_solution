def maxStocks(arr, n, k):
    money_remaining = k
    stocks_bought = 0
    stocks = list(zip(arr, list(range(1, n+1))))
    stocks.sort(key = lambda x: x[1])
    for i in range(n):
        if money_remaining >= stocks[i][0]*stocks[i][1]:
            money_remaining -= (stocks[i][0]*stocks[i][1])
            stocks_bought += stocks[i][0]
        else:
            stocks_bought += (money_remaining//stocks[i][1])
            break
    return stocks_bought

if __name__ == '__main__':
    arr = [7, 10, 4]
    k = 100
    print(maxStocks(arr, len(arr), k))