from itertools import combinations

def printAllSubSeq(se, STR, subSTR=""):
    """To print all subsequences of string concept: Pick and Don’t Pick"""
    if len(STR) == 0:
        if subSTR not in se:
            se.add(subSTR)
            print(subSTR, end=" ")
        return
 
    # we add adding 1st character in string
    printAllSubSeq(se, STR[1:], subSTR + STR[0])
    # Not adding the first character
    printAllSubSeq(se, STR[1:], subSTR)

# Using a python library function
def Sub_Sequences(STR='abc'):
    combs = []
    for l in range(1, len(STR)+1):
        combs.append(list(combinations(STR, l)))
    print(combs)
    for c in combs:
        for t in c:
            print (''.join(t), end =' ')

if __name__ == "__main__":
    s = input()
    printAllSubSeq(set(), s, '')