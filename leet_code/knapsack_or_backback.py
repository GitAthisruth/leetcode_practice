def knapsack_with_repetitions(W, weights, values, n):
    # Initialize the value array
    value = [0] * (W + 1)

    # Iterate over each weight from 1 to W
    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                value[w] = max(value[w], value[w - weights[i]] + values[i])

    return value[W]

# Example usage
if __name__ == "__main__":
    W = 5  # Total weight capacity of the knapsack
    weights = [2, 3, 4, 5]  # Weights of the items
    values = [3, 4, 5, 6]  # Values of the items
    n = len(weights)  # Number of items

    # max_value = knapsack_with_repetitions(W, weights, values, n)
    # print("Maximum value in the knapsack:", max_value)





def knapsack(weights, values, W):
    n = len(weights)
    # Create a 2D array to store the maximum value for each weight and item
    dp = [[0]*(W + 1) for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
max_value = knapsack(weights, values, W)
print("Maximum value in Knapsack =", max_value)