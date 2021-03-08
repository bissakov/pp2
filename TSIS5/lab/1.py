from pathlib import Path
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

entries = Path('C:\\Users\\bissa\\Desktop\\pp2')
for entry in entries.iterdir():
    if entry.is_file():
        print(entry.name + "\tFile\t" + convert_date(entry.stat().st_mtime) + "\t" + str(entry.stat().st_size))
    else:
        print(entry.name + "\tDirectory\t" + convert_date(entry.stat().st_mtime) + "\t")