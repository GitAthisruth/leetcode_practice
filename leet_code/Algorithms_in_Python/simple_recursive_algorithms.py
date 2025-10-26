# factorials


# n = 5
# fact = 1
# for i in range(n-1):
#     fact*=(n-i)
   
# print(fact)


# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact*=i
   
# print(fact)



# def factorila(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorila(n-1)

# print(factorila(0))



# Permutation - arrangement of objects in a specific order. AB !=BA . Consider all orders.

# P(n,r) = n!/(n-r)!

#Combination  - Selection of items form an object . Here AB == BA. 

# C(n,r) = n!/(r!*(n-r)!)

# combination = permutation but without repeating arrangements that differ only by order.




# val = "ABC"

# for 3 letter
# permutation = ABC,ACB,BAC,BCA,CAB,CBA
# combination = ABC 

# permutation


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))

# def permutation(n,r):
#     return factorial(n)//factorial(n-r)


# def combination(n,r):
#     return factorial(n)//factorial(r)*factorial(n-r)

# print(permutation(3,2))
# print(combination(3,2))


# def get_permutations(s):
#     # Base case: if the string has 1 letter, only 1 permutation (itself)
#     if len(s) == 1:
#         return [s]
    
#     result = []
#     for i in range(len(s)):
#         # pick one letter
#         letter = s[i]
#         # remaining letters
#         remaining = s[:i] + s[i+1:]
#         print(f"remaining:{remaining}")
#         # get permutations of the remaining letters
#         print("get inside for loop")
#         for perm in get_permutations(remaining):
#             result.append(letter + perm)
#             print(f"result:letter:{letter}-perm:{perm}")
#             print(f"result:{result}")

#     return result

# print(get_permutations("ABC"))


# from itertools import combinations,permutations

# s = "ABC"
# result = []
# for r in range(1,len(s)+1):
#     for c in combinations(s, r):
#         if ''.join(c) not in result:
#             result.append(''.join(c))
# print(result)


# s = "ABC"
# result = []
# for r in range(1,len(s)+1):
#     for c in permutations(s, r):
#         if ''.join(c) not in result:
#             result.append(''.join(c))
# print(result)


# def per(s):
#     if len(s) == 1:
#         return [s]
    
#     result = []
#     for i in range(len(s)):
#         letter = [s[i]]
#         remaining = s[:i] + s[i+1:]
#         for perm in per(remaining):
#             result.append(letter + perm)
#     return result


# print(per([1,2,3]))

# val = [1,2,3]

# print(val[:1]+val[2:])


# sorting


# def insert_sort(A):
#     for i in range(1, len(A)):
#         key = A[i]
#         j = i - 1
#         while j >= 0 and key < A[j]:
#             A[j + 1] = A[j]
#             j -= 1
#         A[j + 1] = key
#     return A

# A = [12, 11, 13, 5, 6]

# print(insert_sort(A))



# Linked List

# class Node:
#     def __init__(self,element,next = None):
#         self.element = element
#         self.next = next

# node1 = Node(10)
# node2 = Node(20)
# node1.next = node2

# print(node1.element)
# print(node1.next.element)



# class Node:
#     def __init__(self, element):
#         self.element = element
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None  # start of the list

#     def add_at_end(self, element):
#         new_node = Node(element)
#         if self.head is None:        # if list is empty
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:      # go to the end
#                 current = current.next
#             current.next = new_node  # add new node at end

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.element, end=" -> ")
#             current = current.next
#         print("None")


# import numpy as np

# X = np.array([[2,3,4,5],[1,2,3,4]])

# Y = np.array([[2,3],[1,2],[2,3],[1,2]])


# for i in range(len(X)):
#     print(X[i])
#     for j in range(len(X[i])):
#         print(X[i][j])


# Z = np.matmul(X,Y)

# print(Z)


# word = "Malaalam"
# word = word.lower()
# left,right = 0,len(word)-1

# while left<=right:
#     if word[left] == word[right]:
#         left+=1
#         right-=1
       
#     else:
#         print(f"{word} is not a palindrome")
#         break
# else:
#     print(f"{word} a palindrome")   




word = "Malaalam"

# word = word.lower()
# print(word[::-1])
# if word == word[::-1]:
#     print("it is a palindrome")
# else:
#    print("Not a pal")

