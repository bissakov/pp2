#Validating Roman Numerals
#https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

thousand = "M{0,3}"
hundred = "(C[MD]|D?C{0,3})"
ten = "(X[CL]|L?X{0,3})"
digit = "(I[VX]|V?I{0,3})"

print(bool(re.match(thousand + hundred + ten + digit +"$", input())))

print(bool(re.match("M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$", input())))


# regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"    # Do not delete 'r'.

# import re
# print(str(bool(re.match(regex_pattern, input()))))