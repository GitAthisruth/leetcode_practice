# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.



nums = [9,6,4,2,3,5,7,0,1]

list1 = list(range(len(nums)+1))


def missing_num():
    for i in list1:
        if i not in nums:
            return i
    return len(list1)   

    
print(list1)

# print(missing_num())



# method 2

print(sum(nums))
actual_sum = sum(nums)
expected_sum = sum(list1)

print(actual_sum,expected_sum)
missing_val = expected_sum - actual_sum

print(missing_val)

