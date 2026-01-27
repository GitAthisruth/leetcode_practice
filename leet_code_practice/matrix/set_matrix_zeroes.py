# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


matrix = [[1,1,1],[1,0,1],[1,1,1]]

zero_row,zero_col = set(),set() 

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            zero_row.add(i)
            zero_col.add(j)
    
print(zero_row,zero_col)

for j in range(len(matrix[0])):
    for r in zero_row:
        matrix[r][j] = 0


for i in range(len(matrix)):
    for c in zero_col:
        matrix[i][c] = 0

print(matrix)