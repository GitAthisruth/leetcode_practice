nums = [0,1,2,2,3,0,4,2]
val = 2
count = nums.count(val)

nums[:] = [i for i in nums if i!=val]+["_"]*count

print(nums)