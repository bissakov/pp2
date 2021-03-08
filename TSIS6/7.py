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