# Faizan's solution, somewhat Python dependent like able to append, pop and find length
from numpy import array


def tugOfWarUtil(arr, n, idx, s1, s2, res):
    if idx == n:
        cur_res = abs(sum(s1) - sum(s2))
        if res[2] > cur_res:
            res[0] = s1[:]
            res[1] = s2[:]
            res[2] = cur_res
        return

    if len(s1) < n // 2:
        s1.append(arr[idx])
        tugOfWarUtil(arr, n, idx + 1, s1, s2, res)
        s1.pop()
    if len(s2) < (n + 1) // 2:
        s2.append(arr[idx])
        tugOfWarUtil(arr, n, idx + 1, s1, s2, res)
        s2.pop()


# Another solution, if we not need to print the array elements in both the sets and simply want the minimum diff
def tugOfWarHelper(
    arr: list, idx: int, set1: int, set2: int, n_set1: int, min_diff: list
):
    """
    arr  	: List of elements
    idx  	: Current index of the array
    set1 	: Sum of the elements in set1
    set2 	: Sum of the elements in set2
    n_set1	: Number of elements in set1
    min_diff: List of a single element to keep track of min_diff
    Function call tugOfWarHelper(arr, 0, 0, 0, 0, [sys.maxint])
    """
    n = len(arr)
    if idx >= n:
        if abs(set1 - set2) < min_diff[0]:
            min_diff[0] = abs(set1 - set2)
        return
    if n_set1 < (n // 2 + n % 2):
        tugOfWarHelper(arr, idx + 1, set1 + arr[idx], set2, n_set1 + 1, min_diff)
    if (n_set1 - idx) < (n // 2 + n % 2):
        tugOfWarHelper(arr, idx + 1, set1, set2 + arr[idx], n_set1, min_diff)


def tugOfWar(arr, n):
    res = [[], [], float("inf")]
    tugOfWarUtil(arr, n, 0, [], [], res)
    print("Subset 1:", res[0])
    print("Subset 2:", res[1])
    print("Min diff: ", res[2])


arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
n = 11
tugOfWar(arr, n)


# GFG SOLUTION
# Python3 program for above approach

# function that tries every possible
# solution by calling itself recursively
def TOWUtil(
    arr,
    n,
    curr_elements,
    no_of_selected_elements,
    soln,
    min_diff,
    Sum,
    curr_sum,
    curr_position,
):

    # checks whether the it is going
    # out of bound
    if curr_position == n:
        return

    # checks that the numbers of elements
    # left are not less than the number of
    # elements required to form the solution
    if (int(n / 2) - no_of_selected_elements) > (n - curr_position):
        return

    # consider the cases when current element
    # is not included in the solution
    TOWUtil(
        arr,
        n,
        curr_elements,
        no_of_selected_elements,
        soln,
        min_diff,
        Sum,
        curr_sum,
        curr_position + 1,
    )

    # add the current element to the solution
    no_of_selected_elements += 1
    curr_sum = curr_sum + arr[curr_position]
    curr_elements[curr_position] = True

    # checks if a solution is formed
    if no_of_selected_elements == int(n / 2):

        # checks if the solution formed is better
        # than the best solution so far
        if abs(int(Sum / 2) - curr_sum) < min_diff[0]:
            min_diff[0] = abs(int(Sum / 2) - curr_sum)
            for i in range(n):
                soln[i] = curr_elements[i]
    else:

        # consider the cases where current
        # element is included in the solution
        TOWUtil(
            arr,
            n,
            curr_elements,
            no_of_selected_elements,
            soln,
            min_diff,
            Sum,
            curr_sum,
            curr_position + 1,
        )

    # removes current element before returning
    # to the caller of this function
    curr_elements[curr_position] = False


# main function that generate an arr
def tugOfWar(arr, n):

    # the boolean array that contains the
    # inclusion and exclusion of an element
    # in current set. The number excluded
    # automatically form the other set
    curr_elements = [None] * n

    # The inclusion/exclusion array
    # for final solution
    soln = [None] * n

    min_diff = [999999999999]

    Sum = 0
    for i in range(n):
        Sum += arr[i]
        curr_elements[i] = soln[i] = False

    # Find the solution using recursive
    # function TOWUtil()
    TOWUtil(arr, n, curr_elements, 0, soln, min_diff, Sum, 0, 0)

    # Print the solution
    print("The first subset is: ")
    for i in range(n):
        if soln[i] == True:
            print(arr[i], end=" ")
    print()
    print("The second subset is: ")
    for i in range(n):
        if soln[i] == False:
            print(arr[i], end=" ")


# Driver Code
if __name__ == "__main__":

    arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    n = len(arr)
    tugOfWar(arr, n)
