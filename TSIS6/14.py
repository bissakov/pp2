import re

def isPangram(s):
    if len(s) < 26: return False
    else:
        s = s.lower()
        a = sorted(set(re.findall(r"[a-z]",s)))

        if len(a) == 26: return True
        else: return False

s = "The quick brown fox jumps over the lazy dog"

print(isPangram(s))

# import string, sys
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
 
# print ( ispangram('The quick brown fox jumps over the lazy dog')) 