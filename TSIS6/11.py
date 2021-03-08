import math

def allDiv(x):
    l = []
    i = 1
    while i <= math.sqrt(x):
        if x % i == 0:
            if x/i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(x/i)
        i = i + 1
    return l

def isPerfect(n,l):
    sum = 0
    for i in range(0,len(l)):
        sum += int(l[i])

    if n == (sum - n):
        return True
    else: return False

for i in range(0,10000):
    ok = isPerfect(i,allDiv(i))
    if ok:
        print(isPerfect(i,allDiv(i)),i)

# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))