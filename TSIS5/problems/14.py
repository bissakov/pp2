f = open(r"text.txt","r")

l = f.readlines()

f.close()

f = open(r"text2.txt","w")

for x in f:
    i = 0
    for j in range(i,len(l)):
        f.write(l[j])
        break
    i += 1


# with open('abc.txt') as fh1, open('test.txt') as fh2:
#     for line1, line2 in zip(fh1, fh2):
#         # line1 from abc.txt, line2 from test.txtg
#         print(line1+line2)