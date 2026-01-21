nums = [1,2,3,4,2]


def dup(nums):
    seen = {}
    flag = False
    for i,num in enumerate(nums):
        if  num in seen:
            flag = True
            return flag
        else:
            seen[num] = i
    return flag

print(dup(nums))


def du(nums):
    return len(set(nums)) != len(nums)

print(du(nums))