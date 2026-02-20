from stack import Stack

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.




num1 =  Stack()

num1.insert(4)
num1.insert(1)
num1.insert(2)

num2 = Stack()

num2.insert(1)
num2.insert(3)
num2.insert(4)
num2.insert(2)


# print(num1.show())
# print(num2.show())


a,b = [4,1,2],[1,3,4,2]

# output = [-1,3,-1]

def next_greater_element(a,b):   
    result  = []
    for x in a:
        flag = False
        # print(flag)
        val = b.index(x)
        for i in range(val+1,len(b)):
            if b[i]>x:
                result.append(b[i])
                flag = True
                break
        if not flag:
            result.append(-1)
    return result

# print(next_greater_element(a,b))


# rr = {}
# gg = {}
# safe = []
# for i in range(len(b)-1,-1,-1):
#     rr[i] = b.pop()
# for j in range(len(a)-1,-1,-1):
#     gg[j] = a.pop()

# print(rr)
# print(gg)

num1 =  Stack()

num1.insert(4)
num1.insert(1)
num1.insert(2)

num2 = Stack()

num2.insert(1)
num2.insert(3)
num2.insert(4)
num2.insert(2)


def nge(a,b):
    safe = -1
    res = []
    temp = a[:]
    while temp:
        num = temp.pop()
        idx =  b.index(num)
        for i in range(len(b)-1,-1,-1):
            if b[i] == b[idx]:
                break
            if b[i]>num:
                safe = b[i]   
        res.append(safe)
        safe = -1

    return res

# print(nge(a,b))

nums2 = [1,3,4,2]

def nxt_greater_ele(a,b):
    stack = []
    nge = {}#for saving the bigger next element for comparing it num1 with num2 at last. 
    for x in b:
        while stack and x>stack[-1]:
            small = stack.pop()
            nge[small]=x
        stack.append(x)
    while stack:
        nge[stack.pop()]=-1

    return [nge[i] for i in a] 

print(nxt_greater_ele(a,b))




