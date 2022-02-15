def runCustomerSimulation(comps, seq):
    sitting = 0
    occupied = [0] * 26 
    left_without_using = 0
    for customer in seq:
        if occupied[ord(customer) - 65] == 1:
            occupied[ord(customer) - 65] = 0
            sitting -= 1
        elif occupied[ord(customer) - 65] == -1:
            left_without_using += 1
        elif sitting==comps:
            occupied[ord(customer) - 65] = -1
        else:
            occupied[ord(customer) - 65] = 1
            sitting += 1
    return left_without_using

print (runCustomerSimulation(2, "ABBAJJKZKZ") )
print (runCustomerSimulation(3, "GACCBDDBAGEE") )
print (runCustomerSimulation(3, "GACCBGDDBAEE") )
print (runCustomerSimulation(1, "ABCBCA") )
print (runCustomerSimulation(1, "ABCBCADEED") )
        