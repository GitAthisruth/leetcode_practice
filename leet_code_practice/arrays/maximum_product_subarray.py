# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

nums = [2,3,-2,4]
current_product = nums[0]
current_min_product = nums[0]
max_ = nums[0]
for i in range(1,len(nums)):
    n=nums[i]
    if n<0:
        current_min_product,current_product = current_product,current_min_product
    current_product = max(n,current_product*nums[i])
    current_min_product = min(n,current_min_product*nums[i])
    max_ = max(current_product,max_)

print(max_)