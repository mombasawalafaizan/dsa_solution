# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

def numDecodings(s):
    if not s:
        return 0
    n = len(s)
    prev_to_prev = 1
    prev = 1 if s[0] != '0' else 0
    for i in range(2, n+1):
        ans = 0
        first = int(s[i-1:i])
        second = int(s[i-2:i])
        if (first >= 1 and first <= 9):
            ans = (ans + prev)
        if (second >= 10 and second <= 26):
            ans = (ans + prev_to_prev)
        prev_to_prev = prev
        prev = ans
    return prev

# In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

# Given a string s containing digits and the '*' character, return the number of ways to decode it.

# Since the answer may be very large, return it modulo 109 + 7.


def numDecodings2(s: str) -> int:
    n = len(s)
    prev_to_prev = 1
    if s[0] == '*':
        prev = 9
    elif s[0] != '0':
        prev = 1
    mod = 10**9 + 7
    for i in range(2, n+1):
        ans = 0
        first = s[i-1:i]
        second = s[i-2:i]
        if first == '*':
            # In cases like [1-9]* or **
            ans = (ans + prev * 9) % mod
            if second[0] == '1':
                # Number can be from 11-19
                ans = (ans + prev_to_prev * 9) % mod
            elif second[0] == '2':
                # Number can be from 21-26
                ans = (ans + prev_to_prev * 6) % mod
            elif second[0] == '*':
                # Number can be from both the above ranges
                ans = (ans + prev_to_prev * 15) % mod
        else:
            if first != '0':
                ans = (ans + prev) % mod
            if second[0] == '*':
                # In cases like *[0-9]
                if int(first) <= 6:
                    # Number can from 10 to 26, so include both the 2 digits
                    ans = (ans + prev_to_prev * 2) % mod
                else:
                    # Else number can only be from 21 to 26, as in the below case
                    ans = (ans + prev_to_prev) % mod
            elif int(second) >= 10 and int(second) <= 26:
                ans = (ans + prev_to_prev) % mod
        prev_to_prev = prev
        prev = ans

    return prev
