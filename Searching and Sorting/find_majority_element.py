def majorityElement(A,N):
    if N == 0:
        return -1
    if N == 1:
        return A[0]
    cur_el = A[0]
    count = 1
    for j in range(1, N):
        if cur_el == A[j]:
            count += 1
        elif count == 0:
            cur_el = A[j]
            count = 1
        else:
            count -= 1
            
    occur = 0
    for i in range(N):
        if A[i] == cur_el:
            occur+=1
    return cur_el if occur > N//2 else -1