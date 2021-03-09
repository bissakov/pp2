import re

def uniqueList(l):
  temp = []
  for x in l:
    if x not in temp:
      temp.append(x)
  return temp

f = open(r"text.txt","r")

l = re.findall(r"\b\S+\b",f.read())

unique_l = uniqueList(l)

for x in unique_l:
    count = 0
    for y in l:s
        if x == y:
            count += 1
    print(count,end=" ")

# from collections import Counter
# def word_count(fname):
#         with open(fname) as f:
#                 return Counter(f.read().split())

# print("Number of words in the file :",word_count("test.txt"))