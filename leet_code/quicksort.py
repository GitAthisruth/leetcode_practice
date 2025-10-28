ls = [25,2,4,1,100,5,0]
import random
def quicksort(ls):
    if len(ls)<=1:
        return ls
    pivot = ls[len(ls)//2]
    # pivot = random.choice(ls)#for random quicksort
    print(pivot)

    left = [x for x in ls if x<pivot]
    middle = [x for x in ls if x==pivot]
    right = [x for x in ls if x>pivot]

    return quicksort(left) + middle + quicksort(right)

print(quicksort(ls))


