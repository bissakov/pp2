nums = [1,2,3,1,1,3]

x = 0
j = 1
for i in range(0,len(nums)):
	for j in range(0,len(nums)):
		if nums[i] == nums[j] and i < j:
			x = x + 1
		else: continue
print(x)