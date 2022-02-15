def minSwaps(v, n):
    arrpos = [*enumerate(v)]
    print(arrpos)
    swaps = 0
    arrpos.sort(key=lambda x:x[1])
    i = 0
    while i < n:
        # If element is in its correct position
        if i == arrpos[i][0]:
            i += 1
            continue
        # Swap the element with its desired value
        else:
            idx = arrpos[i][0]
            arrpos[i], arrpos[idx] = arrpos[idx], arrpos[i]
        # Until correct element is postioned at its place, repeat so decrement
        # i to repeat the same step
        swaps += 1
        
    return swaps

    # OR USE THIS METHOD WITH MORE SPACE
    # n = len(arr)
    # arrpos = [*enumerate(arr)]
    # arrpos.sort(key=lambda x: x[1])
    # vis = [False for k in range(n)]
    # ans = 0
    # for i in range(n):
    #     if vis[i]==True or arrpos[i][0] == i:
    #         continue

    #     cycle_size = 0
    #     j = i
    #     while vis[j]==False:
    #         vis[j] = True
    #         j = arrpos[j][0]
    #         cycle_size += 1
        
    #     if cycle_size > 0:
    #         ans += (cycle_size-1)

    # return ans
    

if __name__ == "__main__":
    arr = list(map(int, '101 758 315 730 472 619 460 479'.split()))
    print(minSwaps(arr, len(arr)))
