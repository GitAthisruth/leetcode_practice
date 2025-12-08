# from itertools import permutations


# def max_dot_product(first_sequence, second_sequence):
#     max_product = 0
#     for permutation in permutations(second_sequence):
#         dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
#         max_product = max(max_product, dot_product)

#     return max_product


# if __name__ == '__main__':
#     n = int(input())
#     prices = list(map(int, input().split()))
#     clicks = list(map(int, input().split()))
#     assert len(prices) == len(clicks) == n
#     print(max_dot_product(prices, clicks))
    

# print(max_value)


# second method 

prices = [-3,5,6]
clicks = [-1,-2,6]

prices.sort()
clicks.sort()

max_dot_product = sum(x*y for x,y in zip(prices,clicks))

print(max_dot_product)
