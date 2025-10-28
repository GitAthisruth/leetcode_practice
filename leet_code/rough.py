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


ls = [5,6,7,24,1,0,34,200,3,5,6]

def insertion_sort(ls):
    for i in range(1,len(ls)):
        j=i-1
        key = ls[i]
        while j>=0 and key<ls[j]:
            ls[j+1]  = ls[j]
            j-=1
        ls[j+1] = key
    return ls        

print(insertion_sort(ls))