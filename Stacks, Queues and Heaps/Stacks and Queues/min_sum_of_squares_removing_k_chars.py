def getMinimumVal(s: str, k: int) -> int:
    if k >= len(s):
        return 0
    arr = [0] * 27
    for ch in s:
        arr[ord(ch)-97]+=1
    arr.sort(reverse=True)
    end = 0
    while arr[end] > 0:
        end += 1
    j = 0
    modify = 0
    while modify!=k:
        j = 1
        while j<=end and arr[0]==arr[j]:
            j += 1
        reverse = j-1
        while reverse>=0:
            arr[reverse] -= 1
            modify += 1
            if modify==k:
                break
            reverse-=1
    cnt = 0
    for i in range(end):
        cnt += arr[i]**2
    return cnt  

s = 'abccc'
k = 2
print(getMinimumVal(s, k))