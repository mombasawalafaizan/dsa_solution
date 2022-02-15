def square(num):
 
    # Handle negative input
    if (num < 0):
        num = -num

    # Initialize result
    result, times = 0, num

    while (times > 0):
        possibleShifts, currTimes = 0, 1

        while ((currTimes << 1) <= times):
            currTimes = currTimes << 1
            possibleShifts += 1
        print(possibleShifts, bin(currTimes))
        result = result + (num << possibleShifts)
        times = times - currTimes

    return result

# Square of a number using bitwise
# operators


def square(n):

	# Base case
	if (n == 0):
		return 0

	# Handle negative number
	n = abs(n)

	# Get floor(n/2) using
	# right shift
	x = n >> 1

	# If n is odd
	if (n & 1):
		return ((square(x) << 2)
				+ (x << 2) + 1)

	# If n is even
	else:
		return (square(x) << 2)


