# def lcs2(a, b):
#     n = len(a)
#     m = len(b)
#     dp = [[0] * (m + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if a[i - 1] == b[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#     return dp[n][m]



def lcs_memo(a, b):
    n, m = len(a), len(b)
    memo = {}

    def helper(i, j):
        # base case: if one list is exhausted
        if i == n or j == m:
            return 0

        # if already computed
        if (i, j) in memo:
            return memo[(i, j)]

        # if elements match
        if a[i] == b[j]:
            memo[(i, j)] = 1 + helper(i + 1, j + 1)
        else:
            # skip one from either list and take max
            memo[(i, j)] = max(helper(i + 1, j), helper(i, j + 1))

        return memo[(i, j)]

    return helper(0, 0)


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input().strip())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs_memo(a, b))

