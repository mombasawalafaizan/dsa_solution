def isFeasible(A, N, M, max_pages):
    """This function calculates whether at most M student can be allocated
    books such that the total pages for each student is at most max_pages"""
    cur_sum = 0
    student = 1
    for i in range(N):
        if A[i] > max_pages:
            return False
        cur_sum += A[i]
        if cur_sum > max_pages:
            student += 1
            cur_sum = A[i]

    return (
        student <= M
    )  # Less than equal to because in the main function, we are increasing l


# Function to find minimum number of pages.
def findPages(A, N, M):
    # code here
    if M > N:
        return -1

    l = 0
    h = sum(A)
    while l < h:
        mid = (l + h) // 2
        if isFeasible(A, N, M, mid):
            h = mid
        else:
            l = mid + 1
    return h
