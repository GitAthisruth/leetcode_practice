# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

nums1 = [1,2,2,1]
nums2 = [5,2,3,2]

count = len(nums2)
out = []
i=0
while i<count:
    if nums2[i] in nums1 and nums2[i] not  in out:
        out.append(nums2[i])    
    print(i)
    i+=1

print(out)

# print(list(set(nums1)|set(nums2)))
