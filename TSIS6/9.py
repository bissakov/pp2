def ifPrime(x,i):
    if(x <= 1): return False
    if(x == i): return True
    if(x % i == 0): return False

    i = i + 1

    return ifPrime(x,i)

for n in range(0,101):
    ok = ifPrime(n,2)
    if ok: print(ifPrime(n,2),n)
    

# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))

