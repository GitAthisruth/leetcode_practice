# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 
# condition1 - there should be same two elements and the difference of elements indices should be less than or equal to the given k.


# k<=3

k=3
nums = [1,2,3,8]
flag = False
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j] and abs(i-j)<=k:
            print(i,j)
            flag = True
            break
    print("\n")

print(flag)


# method 2


index_saver = {}
flag=False
for i,num in enumerate(nums):
    if num in index_saver and abs(i-index_saver[num])<=k:
        flag = True
    index_saver[num] = i

print(index_saver)

print(index_saver[1])
print(flag)