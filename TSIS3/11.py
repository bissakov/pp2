#Задача №3764. Частотный анализ
#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3764#1

text='''hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme'''

text = text.replace("\n"," ")

a = list(set(text.split(" ")))
keys = []
vals = []

for i in range(0,len(a)):
	keys.append(str(text.count(a[i])))
	vals.append(a[i])

zipped_pairs1 = zip(keys, vals)
 
x = [i for _, i in sorted(zipped_pairs1)]
y = sorted(keys)

for i in reversed(range(0,len(y))):
	for j in reversed(range(0,len(x))):
		if int(y[j]) > int(y[j - 1])
	#print(x[i] + " " + y[i])
