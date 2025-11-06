# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 


# nums = input("add a list of numbers with length must be more than 2 :")
# nums = [int(i) for i in nums.split(",")]
# target = int(input("give the target sum: "))


# def two_sums(nums,target):
#     try:
#         result = []
#         for num in range(len(nums)-1):
#             if nums[num] + nums[num+1] == target:
#                 result.extend([num,num+1])
#         return result
#     except Exception as e:
#         print("Unexpected error:", str(e))
#         return result

# if len(nums)>=2:
#     print(two_sums(nums,target))


# nums = [2,7,11,15]
# target = 9

# result = []
# for num1 in range(len(nums)-1):
#     val1 = nums[num1]
#     for num2 in range(1+num1,len(nums)):
#         print(nums[num2])
#         val2 = nums[num2]
#         if val1 + val2 == target:
#             result.extend([num1,num2])

# print(result)

# nums = [2,7,11,15,7,2,8,1]
# target = 9
# result = set()
# seen = {}

# for i,num in enumerate(nums):
#     complement = target - num
#     if complement in seen:
#         result.add((seen[complement],i))
#     seen[num]=i

# print(result)


nums = [2,7,11,15,7,2,8,1]
nums.sort()
val = []
target = 9
n = len(nums)

left,right = 0,len(nums)-1

while left<right:
    s = nums[left]+nums[right]
    if s<target:
        left+=1
    elif s>target:
        right-=1
    else:
        val.append([left,right])
    left+=1
    right-=1

# print(val)


# best method

