#Detect Floating Point Number
#https://www.hackerrank.com/challenges/introduction-to-regex/problem


import re

t = int(input())
n = []
pattern = ""
for i in range(0,t):
    n.append(input())

for i in range(0,t):
    print(bool(re.match(r"^[\+-]?\d*\.\d+$",n[i])))