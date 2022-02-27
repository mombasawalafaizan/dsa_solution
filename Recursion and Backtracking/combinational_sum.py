def combSumUtil(A, B, cur_soln, final, cur_sum, i):
    if i == len(A) or cur_sum > B:
        return
    if cur_sum == B:
        x = cur_soln.copy()
        final.append(x)
        return
    if (cur_sum + A[i]) <= B:
        cur_soln.append(A[i])
        combSumUtil(A, B, cur_soln, final, cur_sum + A[i], i)
        cur_soln.pop()
    combSumUtil(A, B, cur_soln, final, cur_sum, i + 1)


def combinationalSum2(A, B):
    arr = sorted(set(A))
    res = []

    def helper(idx, B, cur_arr):
        if idx >= len(arr):
            return
        # Selection of elements is only done in this case because as the array is sorted,
        # picking further elements will make B more negative only
        if (B - arr[idx]) >= 0:
            if (B - arr[idx]) == 0:
                res.append(cur_arr + [arr[idx]])
                return
            helper(idx, B - arr[idx], cur_arr + [arr[idx]])  # Pick current element only
            helper(idx + 1, B, cur_arr)  # Don't pick current element and go further

    helper(0, B, [])
    return res


def combinationalSum(A, B):
    """
    :param A: given array A
    :param B: given sum to be achieved
    :return: list containing list of numbers in ascending order, giving the combinational sum
    """
    # code here
    final = []
    combSumUtil(sorted(A), B, [], final, 0, 0)
    return final


print(combinationalSum([7, 2, 6, 5], 16))
