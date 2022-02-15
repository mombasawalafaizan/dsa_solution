def wordBreak(s, dictionary, start, end, cur_s, res, n):
    # print(s[start:end], 'cur_s', cur_s)
    if end==n:
        if s[start:end] in dictionary:
            res.append(cur_s+s[start:end])
        return
    if s[start:end] in dictionary:
        wordBreak(s, dictionary, end, end+1, cur_s+s[start:end]+' ', res, n)
    wordBreak(s, dictionary, start, end + 1, cur_s, res, n)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dictionary = set(input().split())
        s = input()
        res = []
        wordBreak(s, dictionary, 0, 1, '', res, len(s))
        if not res:
            print('Empty')
        else:
            for i in sorted(res):
                print('('+i+')', end='')
            print()