#unsorted list 

ls = [5,67,8,9,23,4,1,0,90]
target = 0

def linear_search(ls,target):
    for i in range(len(ls)):
        if ls[i]==target:
            return i
    return -1


print(linear_search(ls,target))

# recursive way

def linear_search_recursive(ls,target,index=0):
    if index == len(ls):
        return -1
    if ls[index] == target:
        return index
    return linear_search_recursive(ls,target,index+1)

print(linear_search_recursive(ls,target))