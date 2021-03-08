def giveEven(a):
    for i in range(0,len(a)):
        if a[i]%2 == 0:
            print(a[i],end=" ")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

giveEven(a)