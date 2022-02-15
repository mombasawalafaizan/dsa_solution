# NOT WORKING AT GFG
# def minimizeHeights(towers: list, n: int, k: int):
#     if n==1:
#         return 0
#     #Set the range
#     true_min = min(towers)
#     true_max = max(towers)
#     #Decrease the difference
#     min_h = true_min+k 
#     max_h = true_max-k
#     # If the new difference is more, increase both so that the difference remains same
#     if true_max-true_min < max_h-min_h:
#         max_h=true_max+k

#     for i in range(n):
#         #If decrease in height is not possible
#         if towers[i]-k<=0:
#             towers[i]+=k
#             min_h = min(towers[i], min_h)
#             max_h = max(towers[i], max_h)
#         else:
#             # If both increase and decrease is out of range, choose the one which will
#             # expand the range less
#             if towers[i]-k<min_h and towers[i]+k>max_h:
#                 if min_h-(towers[i]-k) > (towers[i]+k)-max_h:
#                     max_h = towers[i]+k
#                     towers[i]+=k
#                 else:
#                     min_h = towers[i]-k
#                     towers[i]-=k
#             # If the above condition is not true then,
#             # the height can be fitted in the [min_h, max_h]
#             elif towers[i]-k>=min_h:
#                 towers[i]-=k
#             else:
#                 towers[i]+=k
#     return max_h-min_h      

def minimizeHeights(arr, n, k):
    if n==1:
        return 0
    arr.sort()
    ans = arr[n-1] - arr[0]
    small = arr[0] + k
    big = arr[0] - k
    if small > big:
        small, big = big, small

    for i in range(1, n):
        subtract = arr[i] - k
        add = arr[i] + k
        if subtract >= small or add <= big:
            continue
        if small - subtract <= add - big:
            small = subtract
        else:
            big = add

    return min(ans, big - small)
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        towers = list(map(int, input().split()))
        print(minimizeHeights(towers, n, k))