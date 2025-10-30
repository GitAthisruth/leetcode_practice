money = 8
coins = [5, 4, 1]

steps = 0  # to count total recursive calls

def change(money, coins, memo=None):
    global steps
    steps += 1   # count each function call

    if memo is None:
        memo = {}
    if money in memo:
        return memo[money]
    if money == 0:
        return 0
    if money < 0:
        return float("inf")

    min_count = float("inf")

    for coin in coins:
        num_of_coins = change(money - coin, coins, memo)
        if num_of_coins + 1 < min_count:
            min_count = num_of_coins + 1
        memo[money] = min_count

    return min_count


result = change(money, coins)
print("Minimum coins:", result)
print("Total recursive calls:", steps)
