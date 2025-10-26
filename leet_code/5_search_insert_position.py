# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4



# nums = [1,3,5,6]

# target = 10

# for index,i in enumerate(nums):
#     if i == target:
#         print(index)
#         break
#     elif (index==len(nums)-1) and i!=target:
#         print(len(nums)+1)
    


nums = [1,3,5,6]
target = 7


def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:             
            return i
        elif nums[i] > target:           
            return i
    return len(nums)          
        
print(searchInsert(nums,target))


# for i in range(len(nums)+1):
#     if nums[i] == target and i < len(nums):
#         print(nums[i],i)
#         break
#     elif nums[i]+1 == target:
#          print(i+1)
#          break
     
     


def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:        # Found target
            return mid
        elif nums[mid] < target:       # Search right half
            left = mid + 1
        else:                          # Search left half
            right = mid - 1

    # If not found, 'left' will be the insert position
    return left