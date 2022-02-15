# Python program to find minimum possible
# time by the car chassis to complete


def carAssembly(a, t, e, x):
    NUM_STATION = len(a[0])
    T1 = [0 for _ in range(NUM_STATION)]
    T2 = [0 for _ in range(NUM_STATION)]
    P1 = [0 for _ in range(NUM_STATION)]
    P2 = [0 for _ in range(NUM_STATION)]
    P1[0] = "1"
    P2[0] = "2"
    T1[0] = e[0] + a[0][0]  # time taken to leave
    # first station in line 1
    T2[0] = e[1] + a[1][0]  # time taken to leave
    # first station in line 2

    # Fill tables T1[] and T2[] using
    # above given recursive relations
    for i in range(1, NUM_STATION):
        if (T1[i - 1] + a[0][i]) <= (T2[i - 1] + t[1][i] + a[0][i]):
            P1[i] = "1"
            T1[i] = T1[i - 1] + a[0][i]
        else:
            P1[i] = "2"
            T1[i] = T2[i - 1] + t[1][i] + a[0][i]

        if (T2[i - 1] + a[1][i]) <= (T1[i - 1] + t[0][i] + a[1][i]):
            P2[i] = "2"
            T2[i] = T2[i - 1] + a[1][i]
        else:
            P2[i] = "1"
            T2[i] = T1[i - 1] + t[0][i] + a[1][i]

    cur_path = "0"
    if (T1[NUM_STATION - 1] + x[0]) <= (T2[NUM_STATION - 1] + x[1]):
        cur_path = "1"
    else:
        cur_path = "2"
    path = cur_path

    for i in range(NUM_STATION - 1, 0, -1):
        if cur_path == "1":
            cur_path = P1[i]
        else:
            cur_path = P2[i]
        path = cur_path + " - " + path
    print("Path: Entry ->", path, "-> Exit")
    # consider exit times and return minimum
    return min(T1[NUM_STATION - 1] + x[0], T2[NUM_STATION - 1] + x[1])


# Instead of using T1 and T2 arrays using 2 variables
def carAssemblySpaceOptimized(a, t, e, x):
    n = len(a[0])

    # Time taken to leave first station
    # in line 1
    first = e[0] + a[0][0]

    # Time taken to leave first station
    # in line 2
    second = e[1] + a[1][0]

    for i in range(1, n):
        up = min(first + a[0][i], second + t[1][i] + a[0][i])
        down = min(second + a[1][i], first + t[0][i] + a[1][i])

        first, second = up, down

    first += x[0]
    second += x[1]

    return min(first, second)


a = [[4, 5, 3, 2], [2, 10, 1, 4]]
t = [[0, 7, 4, 5], [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
# a = [[8, 10, 4, 5, 9],
# [9, 6, 7, 5, 6]]
# t = [[0, 2, 3, 1, 3],
# [0, 2, 1, 2, 2]]
# e = [3, 5]
# x = [2, 1]

print(carAssembly(a, t, e, x))
