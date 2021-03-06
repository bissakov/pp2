def getmult(a):
    mult = 1

    for i in range(0,len(a)):
        mult = a[i] * mult
    
    return(mult)

a = [8, 2, 3, 1, 7]

print(getmult(a))