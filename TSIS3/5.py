#Задача №3853. Большой сдвиг
#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3853#1


a = list(map(int, input().split()))
k = int(input())

k = k%len(a)

s = str(a[-k:] + a[:-k])

s = s.replace("[","")
s = s.replace(",","")
s = s.replace("]","")

print(s)
