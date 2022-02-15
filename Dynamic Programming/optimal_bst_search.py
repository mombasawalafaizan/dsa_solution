def optimalSearchTree(keys, freq, n):
    INT_MAX = 9 * 10**7
    cost = [[0 for _ in range(n)] for _ in range(n)]
    presum = [0] * (n+1)
    for i in range(n):
        cost[i][i] = freq[i]
        presum[i+1] = presum[i] + freq[i]

    for L in range(2, n+1):
        for i in range(n-L+2):
            j = i + L - 1
            if i>=n or j>=n:
                break
            cost[i][j] = INT_MAX
            for r in range(i, j+1):
                c = 0
                if r > i:
                    c += cost[i][r-1]
                if r < j:
                    c += cost[r+1][j]
                # c += sum(freq[i:j+1])
                c += (presum[j+1] - presum[i])
                cost[i][j] = min(cost[i][j], c)

    for i in cost:
        print(i)
    return cost[0][n-1]

if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))