#Задача №3751. Пересечение множеств
#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3751#1

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

print(*sorted(a & b))