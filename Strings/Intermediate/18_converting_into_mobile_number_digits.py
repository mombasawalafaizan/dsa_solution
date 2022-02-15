import math
def whatToPress(char: str)->str:
    if char == ' ':
        return '0'
    if char.isupper():        
        num = ord(char)-65
    else:
        num = ord(char)-97
    if num <= 17:
        return str((num//3)+2)*((num%3)+1)
    if num == 18:
        return '7777'
    elif num>18 and num<25:
        multiplier = num%3 if num%3!=0 else 3
        return str(math.ceil(num/3)+1)*multiplier
    else:
        return '9999'
    
    
s = input()
for i in s:
    print(whatToPress(i), end='')
