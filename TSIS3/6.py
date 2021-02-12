#Задача №3749. Количество различных чисел
#https://informatics.mccme.ru/mod/statements/view.php?id=4535#1


a = list(map(int, input().split()))

a = set(a)

print(len(a))
