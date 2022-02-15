# Interleave means the combination string C from A and B keeping characters in order of A and B

def isInterleave(a: str, b: str, c: str)-> bool:
# Assuming no character is commmon between a and b
    m = len(a)
    n = len(b)
    l = len(c)
    if l!=(m+n):
        return False
    i = 0
    j = 0
    for k in range(l):
        if i<m and a[i]==c[k]:
            i+=1
        elif j<n and b[j]==c[k]:
            j+=1
        else:
            return False
    if i==m and j==n:
        return True
    else:
        return False

if __name__ == '__main__':
    a = input("Enter string 1:")
    b = input("Enter string 2:")
    c = input("Enter string to check for shuffle:")
    print('Is C an interleave of A and B?', isInterleave(a, b, c))