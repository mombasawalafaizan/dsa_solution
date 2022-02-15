# Follows the recursive equation:
# f(n) = f(n-1) + (n-1)*f(n-2)

# DP solution
def countFriendsPairingsDP(n):
        if n==0:
            return 0
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n+1):
            f[i] = (i-1)*f[i-2] + f[i-1]
        print(f)
        return f[n]

# Space optimized solution
def countFriendsPairings(n):
        if n==0:
            return n
        prev_to_prev = 1
        prev = 1
        ans = 1
        for i in range(2, n+1):
            # f[i] = (i-1)*f[i-2] + f[i-1]
            ans = (i-1)*prev_to_prev + prev
            prev_to_prev = prev
            prev = ans
        return ans


print(countFriendsPairings(6))