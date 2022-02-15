# Approach done by FAIZAN, GREEDY APPROACH
def minimumJumps(arr: list, n: int) -> int:
    jumps = 0
    i = 0
    while i < n - 1:
        idx = i
        possibilities = i + arr[i]  # Minimum possibilities to start with
        if (
            possibilities >= n - 1
        ):  # If possibilities reach the end, then jump to the end
            jumps += 1
            break
        # Check for the best possibility(max(j+arr[j])) to consider
        for j in range(i + 1, i + arr[i] + 1):
            # If any possibility reach the end, then take it
            if j + arr[j] >= n - 1:
                idx = j
                break
            if j + arr[j] > possibilities:
                idx = j
                possibilities = j + arr[j]
        # If you can go nowhere from here, quit
        if idx == i:
            return -1
        # Jump to the next index with the most possibilities
        i = idx
        jumps += 1
    return jumps


# DP solution Time: O(n*n) Space: O(n)
def minJumpsDP(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float("inf")

    jumps[0] = 0

    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float("inf")
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float("inf")):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
        print(jumps)
    return jumps[n - 1] if jumps[n - 1] != float("inf") else -1


# O(n) time and O(1) space solution
def minJumps(arr, n):
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    steps = arr[0]
    maxReach = arr[0]
    jumps = 1
    for i in range(1, n):
        if i == n - 1:
            return jumps
        steps -= 1
        maxReach = max(maxReach, i + arr[i])

        if steps == 0:
            jumps += 1
            if maxReach <= i:
                return -1
            steps = maxReach - i
    return jumps


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumpsDP(arr, len(arr)))
