# def josephus(n,k):
#     if n==1:
#         return 1
#     else:
#         return (josephus(n-1,k)+k-1)%n+1

# print(josephus(5,2))


# def josephus(n,k):
#     result = 0
#     for i in range(2,n+1):
#         result = (result+k) %i
#     return result+1

# print(josephus(5,2))

# def josephus1(n,k):
#     people = list(range(1,n+1))
#     index = 0
#     while len(people)>1:
#         print(people)
#         index = (index+k-1)%len(people)
#         people.pop(index)
#     return people[0]
# print(josephus1(5,2))