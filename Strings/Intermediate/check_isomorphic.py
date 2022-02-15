def areIsomorphic(s1,s2):
    mapp1 = [' '] * 256
    mapp2 = [' '] * 256
    n1=len(s1)
    n2=len(s2)
    if n1!=n2:
        return False
        
    for i in range(n1):
        idx1 = ord(s1[i])
        idx2 = ord(s2[i])
        if mapp1[idx1] == ' ' and mapp2[idx2] == ' ':
            mapp1[idx1] = idx2
            mapp2[idx2] = idx1
        elif mapp1[idx1] == ' ' or mapp2[idx2] == ' ' or\
            mapp1[idx1] != idx2 or mapp2[idx2] != idx1:
            return False
    return True