# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

nums = [1,1,1]
k=2
val = 0
subarrays = []
for i in range(len(nums)):
    for j in range(i,len(nums)):
        subarrays.append(nums[i:j+1])
        if sum(nums[i:j+1])==k:
            val+=1

# print(val)
# print(subarrays)

nums = [1,2,3]
prefix_map = {0:1}
count = 0
k=3
count_sum=0
for i in nums:
    count_sum+=i
    # print(count_sum)
    if (count_sum-k) in prefix_map:
        count+=prefix_map[count_sum-k]
    
    prefix_map[count_sum] = prefix_map.get(count_sum,0)+1

print(count)
print(prefix_map)


