class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w

def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    '''
    Items.sort(key = lambda x: x.value/x.weight, reverse = True)
    remaining = W
    profit = 0
    for i in range(n):
        # print(Items[i].value, Items[i].weight)
        if remaining >= Items[i].weight:
            remaining = remaining - Items[i].weight
            profit += Items[i].value
        else:
            profit += (remaining/Items[i].weight)*Items[i].value
            break
    return profit