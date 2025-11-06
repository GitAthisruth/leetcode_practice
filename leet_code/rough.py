nums = [2,7,11,15,1,8,6,9]
target = 9
seen = {}
result = []

for index,num in enumerate(nums):
    compliment = target-num
    if compliment in seen:
        result.append([seen[compliment],index])
    seen[num]=index

print(result)

 


