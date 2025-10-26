# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


nums = [4,3,2,7,8,2,3,1]
length_nums = len(nums) 
nums = list(set(nums))
print(f"nums:{nums}")
print(nums)
real_val = list(range(1,length_nums+1))
print(f"real_val:{real_val}")
missing_val = set(real_val).difference(set(nums))
print(list(missing_val))




