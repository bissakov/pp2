#Re.split()
#https://www.hackerrank.com/challenges/re-split/problem


import re

s = input()

l = re.split(r",|\.",s)

for x in l: print(x)

# regex_pattern = r",|\."	# Do not delete 'r'.

# import re
# print("\n".join(re.split(regex_pattern, input())))