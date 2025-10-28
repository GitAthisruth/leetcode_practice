ls = [25,2,4,1,100,5,0]

def random_quicksort(ls):
    if len(ls)<=1:
        return ls
    pivot = ls[len(ls)//2]

    left = [x for x in ls if x<pivot]
    middle = [x for x in ls if x==pivot]
    right = [x for x in ls if x>pivot]

    return random_quicksort(left) + middle + random_quicksort(right)

print(random_quicksort(ls))


