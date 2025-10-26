# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



nums = [5,4,-1,7,8]

maxsum = 0
subarrays = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        subarrays.append(nums[i:j])
        if sum(nums[i:j]) > maxsum:
            maxsum = sum(nums[i:j])


print(maxsum)
print(subarrays)


# second approach

# nums = [5,4,-1,7,8,90]

# currentsum = nums[0]
# maxsum = nums[0]

# for i in range(1,len(nums)):
#     currentsum = max(nums[i],currentsum+nums[i])
#     maxsum = max(maxsum,currentsum)

# print(maxsum)
