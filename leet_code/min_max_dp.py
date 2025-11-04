def max_value(expression):
    n = len(expression)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]

    # Initialize the tables with the values of the expression
    for i in range(n):
        m[i][i] = M[i][i] = expression[i]

    # Fill the tables
    for s in range(1, n):  # s is the length of the subexpression
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = float('inf'), float('-inf')
            for k in range(i, j):
                a = eval(f"M[{i}][{k}] {expression[k]} M[{k + 1}][{j}]")
                b = eval(f"m[{i}][{k}] {expression[k]} m[{k + 1}][{j}]")
                c = eval(f"M[{i}][{k}] {expression[k]} m[{k + 1}][{j}]")
                d = eval(f"m[{i}][{k}] {expression[k]} M[{k + 1}][{j}]")
                
                M[i][j] = max(M[i][j], a, b, c, d)
                m[i][j] = min(m[i][j], a, b, c, d)

    return M[0][n - 1]

# Example usage
expression = [5, '-', 8, '+', 7, '*', 4,'-',8,'+',9]
print(max_value(expression))