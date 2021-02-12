#Задача №3750. Количество совпадающих
#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3750#1

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

print(len(a.intersection(b)))