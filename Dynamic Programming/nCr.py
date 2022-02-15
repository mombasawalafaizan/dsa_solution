# NOTE: C(n, r) = C(n-1, r) + C(n-1, r-1), for n, r > 0
def nCr(n, r):
    if r > n:
        return 0
    comb = [0] * (r+1)
    mod = 10**9 + 7
    for i in range(n+1):
        prev = 1
        for j in range(min(i, r)+1):
            if j == 0 or j == i:
                comb[j] = 1
            else:
                temp = comb[j]
                comb[j] = (comb[j] + prev) % mod
                prev = temp
    return comb[r]

# O(n) time and O(1) space
def binomialCoefficient(n, k):

	# since C(n, k) = C(n, n - k)
	if (k > n - k):
		k = n - k

	# initialize result
	res = 1

	# Calculate value of [n * (n-1) *---* (n-k + 1)]
	# / [k * (k-1) *----* 1]
	for i in range(k):
		res = res * (n - i)
		res = res / (i + 1)
	return res