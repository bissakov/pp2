f = open(r"text.txt","r")

s = f.read().split("\n")
f.close()

print(s)

# def file_read(fname):
#         txt = open(fname)
#         print(txt.read())

# file_read('test.txt')