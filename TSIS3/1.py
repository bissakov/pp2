#Задача №3828. Четные индексы
#https://informatics.mccme.ru/mod/statements/view.php?id=4163#1

arr = list(map(int, input().split()))

for i in range(0,len(arr),2):
	print(arr[i],end=" ")
