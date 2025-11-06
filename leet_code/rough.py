nums = [2,7,11,15,1,8,6,9]
target = 9

result = []
l,r = 0,len(nums)-1
nums.sort()
while l<r:
    s=nums[l]+nums[r]
    if s==target:
        result.append([l,r])
        l+=1
        r-=1
    elif s<target:
        l+=1
    else:
        r-=1

print(result)
 


