def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
    
def FirstRepeated(string): 
      
    # An integer to store presence/absence 
    # of 26 characters using its 32 bits. 
    checker = 0
   
    pos = 0
    for i in string: 
        val = ord(i) - ord('a'); 
   
        # If bit corresponding to current 
        # character is already set 
        if ((checker & (1 << val)) > 0): 
            return pos 
   
        # set bit in checker 
        checker |= (1 << val) 
        pos += 1
   
    return -1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        occurrence = [False]*26
        flag = True
        for ch in s:
            if ch.islower():
                if occurrence[ord(ch)-97]:
                    print(ch)
                    flag = False
                    break
                occurrence[ord(ch)-97] = True
        if flag:
            print(-1)