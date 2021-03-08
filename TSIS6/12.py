def isPal(s):
    rev_s = ""
    for i in range(0,len(s)):
        rev_s = s[i] + rev_s
    if rev_s == s: return True
    else: return False

s = input()

print(isPal(s))