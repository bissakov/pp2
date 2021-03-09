def uniqueList(l):
  temp = []
  for x in l:
    if x not in temp:
      temp.append(x)
  return temp

a = [1,2,3,3,3,3,4,5]

print(uniqueList(a))