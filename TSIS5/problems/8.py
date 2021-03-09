import re

f = open(r"text.txt","r")

l = re.findall(r"\b\S+\b",f.read())

max_len = len(max(l, key=len))
for word in l:
    if len(word) == max_len:
        print(word)

# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]

# print(longest_word('test.txt'))