# ls = [6,78,100,45,34,23,6,1]

# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if ls[j]<ls[i]:
#             ls[i],ls[j]=ls[j],ls[i]

# print(ls)

# ls = [6,78,100,45,34,23,6,1]
# ls.sort()
# print(ls)  

#Bubble sort

ls = [6,78,100,45,34,23,6,1]

for val1 in range(len(ls)-1):
    for val2 in range(1+val1,len(ls)):
        if ls[val2]<ls[val1]:
            ls[val1],ls[val2] = ls[val2],ls[val1]

# print(ls)



ls = [6,78,100,45,34,23,6,1]

new_val = []
minval=ls[0]

for i in range(1,len(ls)):
    if ls[i]<minval:
        minval = ls[i]
      
# print(minval)

# bs

def find_min_rotated(ls):
    left, right = 0, len(ls) - 1
    while left < right:
        mid = (left + right) // 2
        if ls[mid] > ls[right]:
            left = mid + 1
        else:
            right = mid
    return ls[left]

ls = [4,5,6,7,0,1,2]
# print(find_min_rotated(ls))  # Output: 0

 

A = [4,5,6,7,0,1,2]


def insertion_sort(A):
    for i in range(1,len(A)):
        key =  A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

    return A


# print(insertion_sort(A))