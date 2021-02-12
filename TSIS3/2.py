#Задача №3835. Наименьший положительный
#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3835#1

#Задача №3828. Четные индексы
#https://informatics.mccme.ru/mod/statements/view.php?id=4163#1

arr = list(map(int, input().split()))
min = 1001;

for i in range(0,len(arr)):
	if arr[i] <= 0:
		continue
	else:
		if arr[i] <= min:
			min = arr[i]

print(min)