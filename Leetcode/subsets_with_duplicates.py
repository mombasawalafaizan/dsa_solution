def findSubset(idx, arr, cur, subset):
    if idx == len(arr):
        subset.append(cur)
        return
    findSubset(idx + 1, arr, cur + [arr[idx]], subset)
    if len(cur) == 0 or cur[-1] != arr[idx]:
        findSubset(idx + 1, arr, cur, subset)


subset = []
findSubset(0, [1, 2, 2, 2], [], subset)
print(subset)
