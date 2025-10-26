# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


nums = [3,2,3,2,2,2,3,3,3,3,5,5,5,5,5,5,5,5,1]

count = {}

for i in nums:
    count[i] = count.get(i,0) + 1

print(count)
num = 0
ans1 = 0 
for key,val in count.items():
    if val>num:
        num = val
        ans1 = key
print(ans1)

# method 2

ans2 = max(count,key=count.get)
print(ans2)


# method 3


from collections import Counter

counter = Counter(nums)
print(counter)
ans3 = counter.most_common(1)[0][0]#1 gives most common one element
print(ans3)

# least common

ans4 = counter.most_common()[-1][0]

print(ans4)