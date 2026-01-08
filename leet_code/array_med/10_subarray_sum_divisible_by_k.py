# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 
# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0

nums = [4,5,0,-2,-3,1]
k = 5

# print(nums[5:6])#giving len()+1 get get all elements during slicing.

# subarrays = [nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]

# print(subarrays)

# currsum = nums[0]
# maxsum = nums[0]
# for i in range(1,len(nums)):
#     currsum = max(nums[i],currsum+nums[i])
#     maxsum = max(currsum,maxsum)
#    

# print(maxsum)
# print(count)



nums = [4,5,0,-2,-3,1]


prefix_sum = 0
count = 0
rem_freq = {0:1}
k = 5

for num in nums:
    prefix_sum+=num
    remainder = prefix_sum%k

    if remainder in rem_freq:
        count+=rem_freq[remainder]
        print(f"remainder:{remainder},count:{count}")
        rem_freq[remainder]+=1

    else:
        rem_freq[remainder] = 1


print(rem_freq)
print(count)









