# The problem in computer science terms

# We are given:

# n = total number of people

# k = step (every k-th person is eliminated)

# We need to find:

# The position of the last remaining person (safe position) in the circle.


def josephus1(n,k):
    people = list(range(1,n+1))
    index = 0
    while len(people)>1:
        print(people)
        index = (index+k-1)%len(people)
        people.pop(index)
    return people[0]

# print(josephus1(5,2))

def josephus2(n, k):
    if n == 1:
        return 1
    else:
        return (josephus2(n-1, k) + k - 1) % n + 1

# print(josephus2(2, 2))  # Output: 3


def josephus3(n, k):
    result = 0
    for i in range(2, n+1):
        result = (result + k) % i
    return result + 1

print(josephus3(5, 2))  # Output: 3




