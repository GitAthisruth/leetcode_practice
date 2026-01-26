matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
l = len(matrix[0])
transpose = [[0]*n for i in range(l)]
print(transpose)
print(l)

for i in range(n):
    for j in range(l):
        transpose[j][i]=matrix[i][j]




print(transpose)


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# transpose = list(map(list, zip(*matrix)))
# print(transpose)


