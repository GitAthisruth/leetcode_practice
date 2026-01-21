n = 5
def ftz(n):
    fact = 1
    for i in range(n-1):
        fact*=(n-i)
    count = 0
    while fact %10 == 0:
        fact/=10
        count+=1
    return count

print(ftz(n))