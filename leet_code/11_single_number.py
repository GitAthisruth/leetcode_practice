# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

nums = [0,1,2,2,1,0,8,9,9,0] #bitwise checking,XOR cancels identical bits.

result =  0 # using 0 because it ii the identity element.
for num in nums:
   result^=num
   print(f"num:{num} , result:{result}")
print(result)

#second method

count = {}

for i in nums:
   count[i] = count.get(i,0) + 1

print(count)

for key,val in count.items():
   if val==1:
      print(key)
