def lcs3_memo(a, b, c):
    n, m, p = len(a), len(b), len(c)
    memo = {}

    def helper(i, j, k):
        # base case: if any list is exhausted
        if i == n or j == m or k == p:
            return 0

        # if already computed
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        # if all three elements match
        if a[i] == b[j] == c[k]:
            memo[(i, j, k)] = 1 + helper(i + 1, j + 1, k + 1)
        else:
            # skip one from any sequence and take max
            memo[(i, j, k)] = max(
                helper(i + 1, j, k),
                helper(i, j + 1, k),
                helper(i, j, k + 1)
            )

        return memo[(i, j, k)]

    return helper(0, 0, 0)


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input().strip())
    b = list(map(int, input().split()))
    assert len(b) == m

    p = int(input().strip())
    c = list(map(int, input().split()))
    assert len(c) == p

    print(lcs3_memo(a, b, c))
