import re
import csv

f = open("raw.txt", "r", encoding="utf-8")

all_lines = "".join(f.readlines())

company_name = re.search(r"ДУБЛИКАТ\n(.+)\n", all_lines).group(1)
bin_number = re.search(r"БИН (\d+)",all_lines).group(1)
znm_number = re.search(r"ЗНМ: (\w+)",all_lines).group(1)
kassa = re.search(r"Касса (\d+-\d+)",all_lines).group(1)
check_number = re.search(r"Чек (№\d+)",all_lines).group(1)

item_name = re.findall(r"\d+\.\n(.+)\n",all_lines)

price_for_one = re.findall(r"\d,\d+ x (.+),\d+",all_lines)

amount = re.findall(r"(\d),\d+ x .+,\d+",all_lines)

full_price = re.findall(r"Стоимость\n(.+,).+",all_lines)

items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', all_lines)

for i in range(0,len(price_for_one)):
    if price_for_one[i].find(" ") or full_price[i].find(" "):
        price_for_one[i] = price_for_one[i].replace(" ","")
        full_price[i] = full_price[i].replace(" ","")

print(company_name,bin_number,znm_number,kassa,check_number,item_name,price_for_one,amount,full_price, sep="\n\n")

csv.excel.delimiter = ";"
csv.excel.lineterminator = "\n"

with open("table.csv", "w", encoding="cp1251") as f2:
    writer = csv.writer(f2, csv.excel)
    writer.writerow([company_name])
    writer.writerow([f"BIN number: {bin_number}"])
    #writer.writerow([f'Date: {date}', f'Address: {address}'])
    writer.writerow([item_name])
    writer.writerow([price_for_one])
    writer.writerow([amount])
    writer.writerow([full_price])

with open('table.csv', 'r', encoding='cp1251') as f2:
    for line in csv.reader(f, csv.excel):
        print(line)
