import re
import csv

f = open("raw.txt", "r", encoding="utf-8")

raw = "".join(f.readlines())

company_name = re.search(r"ДУБЛИКАТ\n(.+)\n", raw).group(1)
bin_number = re.search(r"БИН (\d+)",raw).group(1)
znm_number = re.search(r"ЗНМ: (\w+)",raw).group(1)
cashbox = re.search(r"Касса (\d+-\d+)",raw).group(1)
receipt_number = re.search(r"Чек (№\d+)",raw).group(1)

product_name = re.findall(r"\d+\.\n(.+)\n",raw)

unit_price = re.findall(r"\d,\d+ x (.+),\d+",raw)

amount = re.findall(r"(\d),\d+ x .+,\d+",raw)

full_price = re.findall(r"Стоимость\n(.+),.+",raw)

time = re.search(r"Время: (.+)",raw).group(1)

address = re.search(r"г\..+",raw).group()

total = re.search(r"ИТОГО:\n(.+),.+",raw).group(1)
total = total.replace(" ","")

for i in range(0,len(unit_price)):
    if unit_price[i].find(" ") or full_price[i].find(" "):
        unit_price[i] = unit_price[i].replace(" ","")
        full_price[i] = full_price[i].replace(" ","")

csv.excel.delimiter = ","
csv.excel.lineterminator = "\n"

with open("table.csv", "w", encoding="cp1251") as f2:
    writer = csv.writer(f2, csv.excel)
    writer.writerow(["Bin Number","ZNM Number","Cashbox Number","Receipt Number","Company Name", "Product Name", "Unit Price", "Amount", "Full Price", "Address", "Time"])
    for i in range(0,len(product_name)):
        writer.writerow([bin_number,znm_number,cashbox,receipt_number,company_name,product_name[i],unit_price[i],amount[i],full_price[i],address,time])
    writer.writerow(["","","","","","","","","Total: " + str(total),"","",])
    

with open('table.csv', 'r', encoding='cp1251') as f2:
    for line in csv.reader(f, csv.excel):
        print(line)
