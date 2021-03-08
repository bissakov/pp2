def ifInRange(n,a,b):
    if(n > a and n < b): print("YES")
    else: print("NO")

n = int(input())
a = int(input())
b = int(input())
ifInRange(n,a,b)

# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)