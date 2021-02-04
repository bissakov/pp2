n = int(input())

hs = str(int((n%1440)/60))
ms = str(n%60)

print(hs + " " + ms)