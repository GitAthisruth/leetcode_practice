nums = [2,7,11,15]
target = 9


def twoSum(nums,target):
    seen = {}
    val = []
    for i,num in enumerate(nums):
        rem = target - num
        if rem in seen:
            val.extend([seen[rem],i])
        seen[num] = i
    return val





print(twoSum(nums,target))


