nums = [2,7,11,15]
target = 9

l,r = 1, len(nums)-1

result = []
while l<r:
    if nums[l]+nums[r] == target:
        result.extend([l,r])
    else:
        l+=1
    r=-1

print(result)






