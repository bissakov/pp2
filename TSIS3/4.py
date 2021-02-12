#Задача №3850. Сжатие списка
#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3850#1

a = list(map(int, input().split()))
num = 0

for x in a:
	if x != 0:
		print(str(x),end=" ")
		num = num + 1

print('0 '*(len(a)-num))
		
