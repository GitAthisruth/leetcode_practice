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


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
