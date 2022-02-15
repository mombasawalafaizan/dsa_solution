def compare(n1, n2):
    for i in range(len(n1)):
        if int(n1[i]) == int(n2[i]):
            continue
        elif int(n1[i]) > int(n2[i]):
            return True
        else:
            return False
    return True

def findMaxUtil(s, k, max_num, idx):
    if k==0 or idx >= len(s):
        return
    max_ch = s[idx]
    for i in range(idx+1, len(s)):
        if max_ch < s[i]:
            max_ch = s[i]
    if max_ch != s[idx]:
        k -= 1
    for j in range(idx, len(s)):
        if s[j] == max_ch:
            s[idx], s[j] = s[j], s[idx]
            if compare(s, max_num):
                for i in range(len(max_num)):
                    max_num[i] = s[i]
            findMaxUtil(s, k, max_num, idx+1)
            s[idx], s[j] = s[j], s[idx]
    

def findMaximumNum(s,k):
    # s is the input string
    # k is an integer denoting max swaps
    # return the max possible number that can be made in k swaps
    max_num = list(s)
    findMaxUtil(list(s), k, max_num, 0)
    return ''.join(max_num)