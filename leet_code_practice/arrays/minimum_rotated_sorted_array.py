# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


nums = [3,4,5,0,1,2] 

def minbs(nums):
    l,r=0,len(nums)-1
    while l<r:
        m = (l+r)//2
        if nums[m]>nums[r]:
            l=m+1
        else:
            r=m
    return nums[l],l

print(minbs(nums))