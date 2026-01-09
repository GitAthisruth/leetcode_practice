# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6
# Largest sum of a contiguous subarray - means donot broke the order of the original array.

nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray(nums):
    current_sum = nums[0]
    max_ = nums[0]
    for i in range(1,len(nums)):
        current_sum = max(nums[i],current_sum+nums[i])
        max_ = max(current_sum,max_)
    return max_


print(max_subarray(nums))




