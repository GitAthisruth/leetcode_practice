# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"


nums = [0,1,2,4,5,7,8,9]

result = []

if not  result:
    print([])

start = nums[0]

for i in range(1,len(nums)):
    if nums[i] != nums[i-1]+1:
        end=nums[i-1]
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        start = nums[i] 

        
if start == nums[-1]:
    result.append(str(start))
else:
    result.append(f"{start}->{nums[-1]}")

print(result)






nums = [0,1,2,3,4,5,6,7,9]


lm = []

for i in range(1,len(nums)):
    if abs(nums[i-1]-nums[i])>1:
        lm.append(i)


#take the interval points an create final outputs .
# for i in lm:
#     print(i)
print(lm)

v = []
start=0
for i in range(len(lm)):
    v.append(nums[start:lm[i]])
    start = lm[i]
print(start)
if len(lm[start:])>0:
    v.append(nums[lm[-1]:])
print(v)
result = []
for i in range(len(v)):
    if len(v[i])>1:
        result.append(f"{v[i][0]}" + "->"+f"{v[i][-1]}") # In leetcode only .format method accept .
    else:
        result.append(f"{v[i][0]}")
print(result)





# 3th method 





nums = [0,1,2,5,9,11,13,19,20,21]

a = []
start = 0
len_val = 0
for i in range(1,len(nums)):
    if abs(nums[i-1]-nums[i])>1:
        len_val+=len(nums[start:i])
        if nums[start]!=nums[i-1]:
            a.append(f"{nums[start]}->{nums[i-1]}")
        else:
            a.append(f"{nums[i-1]}")
        start=i
        

if len(nums)-len_val!=1:
    a.append(f"{nums[start]}->{nums[len(nums)-1]}")
else:
    a.append(f"{nums[-1]}")


print(a)





def summaryRanges(nums):
    if not nums:
        return []
    a = []
    start = 0
    len_val = 0
    for i in range(1,len(nums)):
        if abs(nums[i-1]-nums[i])>1:
            len_val+=len(nums[start:i])
            if nums[start]!=nums[i-1]:
                a.append("{0}->{1}".format(nums[start],nums[i-1]))
            else:
                a.append("{0}".format(nums[i-1]))
            start=i
                

    if len(nums)-len_val!=1:
        a.append("{0}->{1}".format(nums[start],nums[len(nums)-1]))
    else:
        a.append("{0}".format(nums[-1]))
    return a

print(summaryRanges([0,1,2,4,5,7]))

