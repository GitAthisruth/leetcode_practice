nums = [1,2,3,4,2]

def fd(nums):
    l,r =0,len(nums)-1
    flag = False
    while l<r:
        if nums[l]==nums[r]:
            flag = True
            return flag
        elif nums[l]<nums[r]:
            l=l+1
        else:
            r=r-1
    return flag
    

print(fd(nums))