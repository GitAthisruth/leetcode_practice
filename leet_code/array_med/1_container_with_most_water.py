# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


height = [1,8,6,2,5,4,8,3,7]

capacity = 0
for i in range(len(height)-1):
    for j in range(i+1, len(height)):
        area = (j - i) * min(height[i], height[j])
        if area > capacity:
            capacity = area

print("Max capacity:", capacity)



cap = 0 
left,right = 0 , len(height)-1

while left<right:
    area = (right-left) * min(height[left],height[right])
    cap = max(cap,area)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1

print(cap)


