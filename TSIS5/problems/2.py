f = open(r"text.txt","r")

n = 3

for i in range(0,n):
    print(f.readline(),end="")

f.close()

# def file_read_from_head(fname, nlines):
#         from itertools import islice
#         with open(fname) as f:
#                 for line in islice(f, nlines):
#                         print(line)
# file_read_from_head('test.txt',2)
