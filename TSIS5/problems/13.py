f = open(r"text2.txt","r")

s = f.read()

f.close()

f = open(r"text.txt","w")
f.write(s)