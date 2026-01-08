nums = [2,7,11,15]
target = 9


def twoSum(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        rem = target - num
        if rem in seen:
            return [seen[rem],i]
        seen[num] = i
  





print(twoSum(nums,target))


