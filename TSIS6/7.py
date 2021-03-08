def countLetters(s):
    countLow = 0
    countUp = 0 
    for i in range(0,len(s)):
        if s[i] > "a" and s[i] < "z":
            countLow = countLow + 1
        elif s[i] > "A" and s[i] < "Z":
            countUp = countUp + 1

    print(countLow,countUp,sep="\n")


s = "The quick Brow Fox"

countLetters(s)

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The quick Brown Fox')