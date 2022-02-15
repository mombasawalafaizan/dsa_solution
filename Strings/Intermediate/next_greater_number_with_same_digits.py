# Algorithm:
# Following is the algorithm for finding the next greater number.
# I)  Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously
#     traversed digit. For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9.
#     If we do not find such a digit, then output is “Not Possible”.
# II) Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’.
#     For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.
# III) Swap the above found two digits, we get 536974 in above example.
# IV) Now sort all digits from position next to ‘d’ to the end of number.
#     The number that we get after sorting is the output. For above example, we sort digits in bold 536974.
#     We get “536479” which is the next greater number for input 534976.

def printSolution(a: list):
    for i in a:
        print(i, end=' ')
    print()


def nextGreatPermutation(s: list, n: int):
    i = n-2
    while i != -1:
        if int(s[i]) < int(s[i+1]):
            break
        i -= 1
    # If all in descending order this is the last permutation
    if i == -1:
        printSolution(s[::-1])
        return

    # Get the minimum number greater than s[i] from [i+1, n-1] idx
    j = n-1
    while j != i:
        if int(s[j]) > int(s[i]):
            break
        j -= 1
    s[j], s[i] = s[i], s[j]  # Swap them
    # Sort the elements by reversing them as they are in descending order
    s[i+1:] = s[:i:-1]
    printSolution(s)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().split()
        nextGreatPermutation(s, n)
