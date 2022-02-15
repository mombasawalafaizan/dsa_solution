def findCurNum(n, k):
    if n==1:
        return 0
    n -= 1
    n_partial_fact = n
    while findKthPermutation.cur_k >= n_partial_fact and n > 1:
        n_partial_fact *= (n-1)
        n -= 1
    first_num_idx = findKthPermutation.cur_k // n_partial_fact
    findKthPermutation.cur_k = findKthPermutation.cur_k % n_partial_fact
    return first_num_idx

def findKthPermutation(n, k):
    arr = list(range(1, n+1))
    findKthPermutation.cur_k = k-1
    ans = ''
    for i in range(n):
        idx = findCurNum(n - i, findKthPermutation.cur_k)
        ans = ans + str(arr[idx])
        arr.pop(idx)
    return ans

print(findKthPermutation(4, 9))