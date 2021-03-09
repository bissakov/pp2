f = open(r"text.txt","r")

#s = f.read().split("\n")
#f.readlines()

l = []

for line in f:
    l.append(line)

print(l)

# def file_read(fname):
#         with open(fname) as f:
#                 #Content_list is the list that contains the read lines.     
#                 content_list = f.readlines()
#                 print(content_list)

# file_read(\'test.txt\')