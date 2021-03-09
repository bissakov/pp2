import os

sz = os.path.getsize("text.txt")
#os.stat("text.txt").st_size 

print(str(sz) + " Bytes")

# def file_size(fname):
#         import os
#         statinfo = os.stat(fname)
#         return statinfo.st_size

# print("File size in bytes of a plain file: ",file_size("test.txt"))