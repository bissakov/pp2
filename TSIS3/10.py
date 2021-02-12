#Задача №3760. Словарь синонимов
#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3760#1

key = []
val = []

n = int(input())
str = ""

i = 0
while i < n:
	str = input()
	key.append(str[0:str.find(" ")])
	val.append(str[str.find(" ")+1:len(str)])
	i = i + 1

word = input()

if word in key:
	print(val[key.index(word)])
elif word in val:
	print(key[val.index(word)])
