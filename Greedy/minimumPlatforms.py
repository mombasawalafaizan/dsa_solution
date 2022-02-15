def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
        
    temp = [0] * 2400
    for i in range(n):
        temp[int(arr[i])] += 1
        temp[int(dep[i])+1] -= 1
        
    required_platforms = 0
    for i in range(1, 2400):
        temp[i] += temp[i-1]
        if temp[i] > required_platforms:
            required_platforms = temp[i]
    return required_platforms


# Program to find minimum
# number of platforms 
# required on a railway
# station

# Returns minimum number
# of platforms reqquired
def findPlatform(arr, dep, n):

    # Sort arrival and
    # departure arrays
    arr.sort()
    dep.sort()
 
    # plat_needed indicates
    # number of platforms
    # needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0
 
    # Similar to merge in
    # merge sort to process 
    # all events in sorted order
    while (i < n and j < n):
   
        # If next event in sorted
        # order is arrival, 
        # increment count of
        # platforms needed
        if (arr[i] <= dep[j]):
        
            plat_needed+= 1
            i+= 1
        
 
        # Else decrement count
        # of platforms needed
        elif (arr[i] > dep[j]):
        
            plat_needed-= 1
            j+= 1

        # Update result if needed 
        if (plat_needed > result): 
            result = plat_needed
        
    return result

# driver code

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",
        findPlatform(arr, dep, n))

# This code is contributed
# by Anant Agarwal.
