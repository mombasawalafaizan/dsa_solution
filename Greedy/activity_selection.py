def printMaxActivities(s, f, n):
    # Sort with respect to finish time
    atvts_sorted = sorted(zip(s, f), key=lambda x: x[1])
    idx = 0
    print("Activities that can be done: 0", end=" ")
    for i in range(1, n):
        if atvts_sorted[i][0] >= atvts_sorted[idx][1]:
            print(i, end=" ")
            idx = i
    print()


if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    n = len(s)
    printMaxActivities(s, f, n)
