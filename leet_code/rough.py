nums = [0,1,2,5,6,7,10,11,12,99]


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
v.append(nums[lm[i]:])
print(v)
result = []
start = 0
end = -1
for i in range(len(v)):
    if len(v[i])>1:
        result.append(f"{v[i][start]}" + "->"+f"{v[i][end]}")
    else:
        result.append(f"{v[i][start]}")
print(result)