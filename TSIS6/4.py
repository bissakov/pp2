def reverseStr(s):
    rev_s = ""
    for i in reversed(range(0,len(s))):
        rev_s = rev_s + s[i]
    return rev_s

s = "1234abcd"

print(reverseStr(s))