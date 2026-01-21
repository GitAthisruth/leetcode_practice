# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

nums = [2,3,-2,4]
current_product = nums[0]
max_ = nums[0]
for i in range(1,len(nums)):
    current_product = max(nums[i],current_product*nums[i])
    max_ = max(current_product,max_)

print(max_)