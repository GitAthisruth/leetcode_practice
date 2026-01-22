# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.



nums = [-100,-70,-60,110,120,130,160]
nums.sort()
n = len(nums)
val = []


for i in range(n):
    if i>0 and nums[i] == nums[i-1]:
        continue
    left,right = i+1,n-1
    while left<right:
        s = nums[i]+nums[left]+nums[right] 
        if s<0:
            left+=1
        elif s>0:
            right-=1
        else:
            val.append([nums[i], nums[left], nums[right]])
            
            # Move pointers inward to look for the next unique pair
            left += 1
            right -= 1

            # 5. Skip any duplicate values to avoid duplicate triplets
            # This is the correct way to handle this
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
print(val)




def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        i = 0

        while i < n-2:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            j = i+1
            k = n-1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    result.append([nums[i],nums[j],nums[k]])

                    j+=1
                    k-=1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1

                elif s < 0:
                    j+=1
                else:
                    k-=1

            i+=1

        return result