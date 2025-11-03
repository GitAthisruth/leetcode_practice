# def change(money,coins,memo=None):
#     if memo is None:
#         memo = {}
#     if money in memo:
#         return memo[money]
#     if money == 0:
#         return 0
#     if money < 0:
#         return float('inf')
    
#     min_coin = float("inf")

#     for coin in coins:
#         num_coin = 1 + change(money-coin,coins,memo)
#         if num_coin<min_coin:
#             min_coin=num_coin
        
#     memo[money] = min_coin


#     return min_coin




def change(money):
    coins = [1, 3, 4]
    dp = [float("inf")] * (money + 1)
    dp[0] = 0
    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))
