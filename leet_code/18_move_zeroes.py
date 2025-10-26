# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


nums = [0,1,0,3,12]

for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(0)

        

print(nums)


# method2


nums1 = [0,1,0,3,12]
nums1.sort(key = lambda x: x==0)

print(nums1)


# method3

nums2 = [1,0,1,0,3,12]

point = 0

for i in range(len(nums2)):
    if nums2[i]!=0:
        nums2[point],nums2[i]=nums2[i],nums2[point]
        point +=1

print(nums2)

# nums2 = [1,0,0,3,12]
# nums2 = [1,3,0,0,12]
# nums2 = [1,3,12,0,0]


