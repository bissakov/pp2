#Validating and Parsing Email Addresses
#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

n = int(input())
l = []

for i in range(0,n):
    l.append(input())

for i in range(0,len(l)):
    if re.search(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>",l[i]): print(l[i])