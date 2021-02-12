#Задача №3753. Кубики
#https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3753#1

n, m = input().split()

n = int(n)
m = int(m)

a = []
b = []

i = 0
j = 0
while i < n:
	a.append(int(input()))
	i = i + 1

while j < m:
	b.append(int(input()))
	j = j + 1

a = set(sorted(a))
b = set(sorted(b))

print(len(a.intersection(b)))
print(*sorted(a & b))
print(len(a.difference(b)))
print(*sorted(a.difference(b)))
print(len(b.difference(a)))
print(*sorted(b.difference(a)))