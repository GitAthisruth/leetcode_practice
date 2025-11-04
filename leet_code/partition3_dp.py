from sys import stdin

def partition3(values):
    total = sum(values)
    n = len(values)

    # If total sum not divisible by 3, impossible
    if total % 3 != 0:
        return 0

    target = total // 3

    # Initialize 3D DP table
    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        val = values[i - 1]
        for j in range(target + 1):
            for k in range(target + 1):
                dp[i][j][k] = dp[i - 1][j][k]  # don’t take item i-1
                if j >= val and dp[i - 1][j - val][k]:
                    dp[i][j][k] = True
                if k >= val and dp[i - 1][j][k - val]:
                    dp[i][j][k] = True

    return 1 if dp[n][target][target] else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
