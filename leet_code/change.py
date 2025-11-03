lis = [6,4,1]
print(sorted(lis,reverse=True))
money = 8

# def change(lis,money):
#     lis.sort(reverse=True)
#     val = 0
#     result = []
#     while money!=0:
#         if lis[val]<=money:
#             money-=lis[val]
#             print(money)
#             result.append(lis[val])
#         else:
#             val+=1

#     return result

# # print(change(lis,money))





# def get_change(money, coins):
#     # Base case
#     if money == 0:
#         return 0
    
#     # If money < 0, we can't make this amount
#     if money < 0:
#         return float('inf')  # infinity = invalid large number
    
#     # Try using each coin
#     min_coins = float('inf')
#     for coin in coins:
#         num_coins = get_change(money - coin, coins)
#         if num_coins + 1 < min_coins:
#             min_coins = num_coins + 1
    
#     return min_coins





def get_change(money, coins, memo=None):
    if memo is None:
        memo = {}

    if money in memo:
        return memo[money]
    if money == 0:
        return 0
    if money < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        num_coins = get_change(money - coin, coins, memo)
        if num_coins + 1 < min_coins:
            min_coins = num_coins + 1

    memo[money] = min_coins
    return min_coins


print(get_change(money,lis))