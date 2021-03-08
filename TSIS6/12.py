def isPal(s):
    rev_s = ""
    for i in range(0,len(s)):
        rev_s = s[i] + rev_s
    if rev_s == s: return True
    else: return False

s = input()

print(isPal(s))

# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('aza')) 