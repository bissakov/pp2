def sortAlph(s):
    l = sorted(s.split("-"))
    temp = ("-").join(l)
    return temp

s = "green-red-yellow-black-white"

print(sortAlph(s))