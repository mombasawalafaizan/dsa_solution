# GFG solution:
# Algorithm: areRotations(str1, str2)

#     1. Create a temp string and store concatenation of str1 to
#        str1 in temp.
#                           temp = str1.str1
#     2. If str2 is a substring of temp then str1 and str2 are 
#        rotations of each other.

#     Example:                 
#                      str1 = "ABACD"
#                      str2 = "CDABA"

#      temp = str1.str1 = "ABACDABACD"
#      Since str2 is a substring of temp, str1 and str2 are 
#      rotations of each other.
#   To find substring find string functions like count, find, index or in operator

def isRotation(s1: str, s2: str)->bool:
    l1 = len(s1)
    l2 = len(s2)
    if l1!=l2:
        return False
    for k in range(l1):
        ptr = k
        j = 0
        while j < l1:
            if s2[j]!=s1[ptr]:
                break
            ptr = (ptr + 1) % l1
            j += 1
        if j==l1-1:
            return True
    return False

if __name__ == '__main__':
    s1, s2 = input().split()
    print('Are s1 and s2 rotation of each other?', isRotation(s1, s2))