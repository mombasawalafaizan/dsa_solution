from heapq import heapify, heappop, heapreplace
def findMinimumCost(arr, n):
    heapify(arr)
    cost = 0
    while True:
        a = heappop(arr)
        if not arr:
            break
        cost += (a + arr[0])
        heapreplace(arr, arr[0] + a)
    return cost
        
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(findMinimumCost(arr, n))