#Validating phone numbers
#https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())
l = []

for i in range(0,n):
    l.append(input())

for i in range(0,len(l)):
    if re.fullmatch(r"[7-9][0-9]{9}",l[i]): print("YES")
    else: print("NO")