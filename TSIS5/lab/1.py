from pathlib import Path
from datetime import datetime
import os

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
                if i % 4 == 0 and i != 0:
                    t += ","
                t += fsize[i-1]
            if len(t[::-1]) < 9: return (9-len(t[::-1]))*" " + t[::-1] + " KB"                
            else: return t[::-1] + " KB"
        else:
            if len(fsize) < 9: return (9-len(fsize))*" " + fsize + " KB"
            else: return fsize + " KB"
    else:
        if len(str(n)) < 9: return (10-len(str(n)))*" " + str(n) + " B"
        else: return str(n) + " B"
    

thisdict = {}

root = "C:\\Users\\bissa\\Downloads"

entries = Path(root)
i = 1
print("#\tName\t\t\t\tType\t\tDate Modified\t   File Size")
for entry in entries.iterdir():
    nameFD = entry.name
    if len(nameFD) >= 23:
         nameFD = nameFD[0:20] + "..." + "\t"
    else: nameFD = nameFD + " "*(23-len(nameFD)) + "\t"

    thisdict[i] = entry.name

    if entry.is_file():
        print(str(i) + "\t" + nameFD + "\tFile\t \t" + convert_date(entry.stat().st_mtime) + "\t   " + convertBytes(entry.stat().st_size))
        i += 1
    else:
        sz = get_size(root + "\\" + entry.name)
        print(str(i) + "\t" +  nameFD + "\tDirectory\t" + convert_date(entry.stat().st_mtime) + "\t   " + convertBytes(sz))
        i += 1

print("\nType file or directory index")
num = int(input())

print(Path(root + "\\" + thisdict[num]).name)