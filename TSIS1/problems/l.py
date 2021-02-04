n = int(input())

h = int(int(n/3600)%24)
m = int((n-int(n/3600)*3600)/60)
s = int((n-int(n/3600)*3600)%60)

print(str(h) + ":" + str(int(m/10)) + str(m%10) + ":" + str(int(s/10)) + str(s%10))