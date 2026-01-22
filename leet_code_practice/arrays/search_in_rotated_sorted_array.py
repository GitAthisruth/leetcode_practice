nums = [4,5,6,7,0,1,2]
target = 0

def bs_v(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)//2

        if nums[m]==target:
            return m
        
        elif nums[l]<=nums[m]:
            if nums[l]<=target<nums[m]:
                r=m-1
            else:
                l=m+1

        else:
            if nums[m]<target<=nums[r]:
                l=m+1
            else:
                r=m-1

    return -1


print(bs_v(nums,target))
