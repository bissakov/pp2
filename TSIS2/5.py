#1281. Subtract the Product and Sum of Digits of an Integer
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution(object):
    def subtractProductAndSum(self, n):
        s = str(n)
        pr = 1
        sm = 0
        for i in range(0,len(s)):
        	pr *= int(s[i])
        	sm += int(s[i])
        return pr - sm