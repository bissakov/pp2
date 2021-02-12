#Задача №3764. Частотный анализ
#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3764#1

tekeyst='''hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme'''

tekeyst = tekeyst.replace("\n"," ")

a = list(set(tekeyst.split(" ")))
keys = []
vals = []

for i in range(0,len(a)):
	keys.append(str(tekeyst.count(a[i])))
	vals.append(a[i])

print(keys)
print(vals)

zipped_pairs1 = zip(keys, vals)
 
x = [i for _, i in sorted(zipped_pairs1)]
y = sorted(keys)

for i in reversed(range(0,len(x))):
	print(x[i] + " " + y[i])
