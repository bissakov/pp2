h = int(input())
a = int(input())
b = int(input())

H = h - a
razn = a - b

x = 1+(H//razn) + (H%razn+razn-1)//razn

print(x)