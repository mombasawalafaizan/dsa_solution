def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    i = 0
    r = 0
    ans = ''

    while r < numRows and r < len(s):
        i = r
        while i < len(s):
            ans += s[i]
            if (i+2*(numRows-r-1)) < len(s) and r != numRows-1 and r != 0:
                ans += s[i+2*(numRows-r-1)]
            i += 2*(numRows-1)
        r += 1

    return ans


print(convert("faizanisag", 2))
