# ls = [25,2,4,1,100,5,0]
import random
def randomized_quick_sort(ls):
    if len(ls)<=1:
        return ls
    # pivot = ls[len(ls)//2]
    pivot = random.choice(ls)#for random quicksort

    left = [x for x in ls if x<pivot]
    middle = [x for x in ls if x==pivot]
    right = [x for x in ls if x>pivot]
    return  randomized_quick_sort(left)+middle + randomized_quick_sort(right)

# print(randomized_quick_sort(ls))


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    val = randomized_quick_sort(elements)
    print(*val)