# nPr = n! / (n-r)!

# Using DP O(n*r) and O(r) space

# NOTE: P(n, k) = P(n-1, k) + k * P(n-1, k-1) 
def permutationCoeffDP(n, r):
    P = [[0 for _ in range(r+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(r+1):
            if j == 0:
                P[i][j] = 1
            else:
                P[i][j] = P[i-1][j] + (j*P[i-1][j-1])
            
            if j < r:
                P[i][j+1] = 0
    return P[n][r]



# A O(n) solution that uses  
# table fact[] to calculate  
# the Permutation Coefficient 
  
# Returns value of Permutation 
# Coefficient P(n, k) 
def permutationCoeff(n, k): 
    fact = [0 for i in range(n + 1)] 

    # base case 
    fact[0] = 1

    # Calculate value  
    # factorials up to n 
    for i in range(1, n + 1): 
        fact[i] = i * fact[i - 1] 

    # P(n, k) = n!/(n-k)! 
    return int(fact[n] / fact[n - k]) 


# A O(n) time and O(1) extra  
# space solution to calculate 
# the Permutation Coefficient 

def PermutationCoeff(n, k): 
    Fn = 1

    # Compute n! and (n-k)! 
    for i in range(1, n + 1): 
        Fn *= i 
        if (i == n - k): 
            Fk = Fn 

    coeff = Fn // Fk 
    return coeff 