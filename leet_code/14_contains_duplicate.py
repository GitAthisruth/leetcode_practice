# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true


ls=[1,2,3,4]

flag = False

for i in range(len(ls)):
    if ls[i] in ls[i+1:]:
        flag = True
        break

print(flag)

# method 2

seen = set()
flag = False
for i in ls:
    if i in seen:
        flag = True
        break
    seen.add(i)

print(flag)
