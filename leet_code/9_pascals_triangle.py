# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


# print([1]*1)
# print(list(range(1,1)))

# triangle = []

# for r in range(10):
#     row = [1] * (r + 1)
#     print(row)
#     for c in range(1,r): #only value above  1will take here.
#         print(f"r:{r},c:{c}")
#         row[c] = triangle[r-1][c-1] + triangle[r-1][c]
#         print(f"triangle[r-1][c]:{triangle[r-1][c-1]}+{triangle[r-1][c]}")
#     triangle.append(row)
#     print(triangle)
#     print("\n")
# print(f'row:{row}')





triangle = []

for i in range(3):
    row = [1]*(i+1)
    for j in range(1,i):#for taking the middle values.
        row[j]= triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

print(triangle)

