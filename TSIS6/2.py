def getSum(a):
    sum = 0

    for i in range(0,len(a)):
        sum = a[i] + sum
    
    return(sum)


a = [8, 2, 3, 0, 7]



print(getSum(a))