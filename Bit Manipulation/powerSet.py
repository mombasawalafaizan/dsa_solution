def AllPossibleStrings(s):
    subsets = []
    n = len(s)
    for counter in range(1, 2**n):
        subset = ''
        for j in range(n):
            if (1<<j) & counter:
                subset += s[j]
        subsets.append(subset)
    # subsets.sort()
    return subsets

print(AllPossibleStrings('xyz'))