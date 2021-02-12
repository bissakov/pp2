#Задача №3840. Переставить в обратном порядке
#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3840#1

arr1 = list(map(int, input().split()))
arr2 = []

for i in range(0,len(arr1)):
	arr2.append(arr1[len(arr1)-i-1])

arr1 = arr2

for i in range(0,len(arr1)):
	print(arr1[i],end=" ")
