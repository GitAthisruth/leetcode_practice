ls = [3,6,8,9,20,0,2]


def splitting_ls(ls):
    if len(ls)<=1:
        return ls
    mid = len(ls)//2
    left = splitting_ls(ls[:mid])
    right = splitting_ls(ls[mid:])
    return merge(left,right)



def merge(left,right):
    i=j=0
    result = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

#merge sort is best sorting algorithm with time complexity O(nlogn))

print(splitting_ls(ls))




# The list [8,9,5,4,20] is first split into [8,9] and [5,4,20].
# The left side [8,9] splits into [8] and [9], which merge to [8,9].
# The right side [5,4,20] splits into [5] and [4,20]; [4,20] itself splits into [4] and [20] and merges to [4,20].
# Then [5] and [4,20] merge to [4,5,20].
# Finally, the two sorted halves [8,9] and [4,5,20] are merged together by comparing elements one by one to form the fully sorted list [4,5,8,9,20].

