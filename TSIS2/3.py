#1512. Number of Good Pairs
#https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
    	x = 0
        j = 1
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] == nums[j] and i < j:
                    x = x + 1
                else: continue
        return x