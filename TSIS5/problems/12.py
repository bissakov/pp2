colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

f = open(r"text2.txt","w")

for color in colors:
    f.write(color + "\n")

f.close()

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open('abc.txt', "w") as myfile:
#         for c in color:
#                 myfile.write("%s\n" % c)

# content = open('abc.txt')
# print(content.read())