def singleNumber(arr):
    # Code here
    sums = 0
    n = len(arr)

    for i in range(0, n):

        # Xor all the elements of the array
        # all the elements occuring twice will
        # cancel out each other remaining
        # two unnique numbers will be xored
        sums = sums ^ arr[i]

        # Bitwise & the sum with it's 2's Complement
        # Bitwise & will give us the sum containing
        # only the rightmost set bit
        sums = sums & -sums

        # sum1 and sum2 will contains 2 unique
        # elements elements initialized with 0 box
        # number xored with 0 is number itself
        sum1 = 0
        sum2 = 0

        # Traversing the array again
        for i in range(0, len(arr)):

            # Bitwise & the arr[i] with the sum
            # Two possibilities either result == 0
            # or result > 0
            if (arr[i] & sums) > 0:

                # If result > 0 then arr[i] xored
                # with the sum1
                sum1 = sum1 ^ arr[i]

            else:

                # If result == 0 then arr[i]
                # xored with sum2
                sum2 = sum2 ^ arr[i]
    return [sum1, sum2]


print(singleNumber([1, 2, 4, 3, 5, 4, 5, 3]))
