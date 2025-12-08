from sys import stdin

def maximum_gold(capacity, weights):
    n = len(weights)
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]  # not taking item i-1
            if weights[i - 1] <= w:
                val = dp[i - 1][w - weights[i - 1]] + weights[i - 1]
                dp[i][w] = max(dp[i][w], val)

    return dp[n][capacity]


# if __name__ == '__main__':
#     input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
#     assert len(input_weights) == n
#     print(maximum_gold(input_capacity, input_weights))






def knapsack(weights, values, capacity):
    n = len(weights)

    # dp[i][w] = max value using first i items with weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):        # items 1..n
        for w in range(1, capacity + 1):  # capacity 1..W

            # Option 1: Don't take item i-1
            # dp[i][w] = dp[i - 1][w]

            # Option 2: Take item i-1 (if weight fits)
            if weights[i - 1] <= w:
                include_value = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                dp[i][w] = max(dp[i][w], include_value)

    return dp[n][capacity]



# weights = [2, 3, 4, 5]
# values  = [3, 4, 5, 6]
# capacity = 5

# print(knapsack(weights, values, capacity))
