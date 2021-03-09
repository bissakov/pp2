f = open(r"text.txt","a")

s = "\nHello World"

f.write(s)

f = open("text.txt", "r")
print(f.read())
f.close()

# def file_read(fname):
#         from itertools import islice
#         with open(fname, "w") as myfile:
#                 myfile.write("Python Exercises\n")
#                 myfile.write("Java Exercises")
#         txt = open(fname)
#         print(txt.read())
# file_read('abc.txt')