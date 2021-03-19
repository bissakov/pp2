from pathlib import Path
from datetime import datetime
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def convertBytes(n):
    #kb
    if n >= 1024:
        fsize = str(round(n/1024))
        t = ""
        if len(fsize) > 3:
            fsize = fsize[::-1]
            for i in range(1,len(fsize)+1):
                if i % 4 == 0 and i != 0: t += ","
                t += fsize[i-1]
            if len(t[::-1]) < 9: return (9-len(t[::-1]))*" " + t[::-1] + " KB"                
            else: return t[::-1] + " KB"
        else:
            if len(fsize) < 9: return (9-len(fsize))*" " + fsize + " KB"
            else: return fsize + " KB"
    else:
        if len(str(n)) < 9: return (10-len(str(n)))*" " + str(n) + " B"
        else: return str(n) + " B"

def shrinkName(s):
    if len(s) >= 23: return s[0:20] + "..." + "\t"
    else: return s + " "*(23-len(s)) + "\t"

root = "D:\\D Misc\\New folder (2)"

while True:
    refName = {}

    entries = Path(root)
    i = 1
    print("\n" + root + "\n\n#\tName\t\t\t\tType\t\tDate Modified\t      File Size")
    for entry in entries.iterdir():
        nameFD = entry.name
        nameFD = shrinkName(nameFD)

        refName[i] = entry.name

        if entry.is_file():
            print(str(i) + "\t" + nameFD + "\tFile\t \t" + convert_date(entry.stat().st_mtime) + "\t   " + convertBytes(entry.stat().st_size))
            i += 1
        else:
            #sz = get_size(root + "\\" + entry.name)
            print(str(i) + "\t" +  nameFD + "\tDirectory\t" + convert_date(entry.stat().st_mtime) + "\t   ")
            i += 1
    
    print("\nType \"return\" to go up to the folder OR select file or directory by typing an index")
    temp = input()
    if temp.lower() == "return":
        if root == "D:\\":
            root = "C:\\"
            continue
        elif root == "C:\\":
            root = "D:\\"
            continue
        root = root[0:root.find(Path(root).name)]
        time.sleep(1.5)
        continue
    else:
        num = temp
        if num.isdigit() == False:
            cls()
            continue
        else: num = int(num)     

    FDroot = root + "\\" + refName[num]

    if Path(FDroot).is_file():
        print("\nDelete File/Rename File/Add to File/Rewrite File/Return to parent directory")
        inp = input().lower()
        if inp == "delete":
            os.remove(FDroot)
            print("File " + Path(FDroot).name + " deleted")
            time.sleep(1.5)
        elif inp == "rename":
            tempNew = root + "\\" + input() + Path(FDroot).suffix
            os.rename(FDroot,tempNew)
            FDroot = root + "\\" + tempNew
            print("File renamed to " + Path(FDroot).name)
            time.sleep(1.5)
        elif inp == "add":
            print("Append to file:")
            with open(FDroot, "a") as myfile:
                myfile.write(input())
            time.sleep(1.5)
        elif inp == "rewrite":
            print("Rewrite the file:")
            with open(FDroot, "w") as myfile:
                myfile.write(input())
            time.sleep(1.5)
        else:
            cls()
            continue
    else:
        print("\nRename Directory/Print number of files/Print number of directories/List content/Add file to/Add new dir")
        inp = input().lower()
        if inp == "rename":
            tempNew = root + "\\" + input() + Path(FDroot).suffix
            os.rename(FDroot,tempNew)
            FDroot = root + "\\" + tempNew
            time.sleep(1.5)
        elif inp == "list":
            root = FDroot
            time.sleep(1.5)
        elif inp == "create file":
            filename = root + "\\" + input()
            with open(filename, "w") as myfile:
                myfile.write("")
            time.sleep(1.5)
        elif inp == "create dir":
            os.mkdir(root + "\\" + input())
            time.sleep(1.5)
        else:
            cls()
            continue
    cls()
