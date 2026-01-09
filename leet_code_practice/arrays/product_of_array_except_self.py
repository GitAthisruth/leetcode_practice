# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Explanation: For each element in the array, compute the product of all other elements except itself without using division and in O(n) time.

from math import prod

nums = [1,2,3,4]


def pa(nums):
    val = []
    for i in range(len(nums)):
        p = prod(nums[:i]+nums[i+1:])
        val.append(p)
    return val

# print(pa(nums)) 

# T(n) = O(n^2)


n = len(nums)
result = [1] * n

# Prefix products
prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= nums[i]

# print(result)

# Suffix products

suffix = 1
for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

# print(result)