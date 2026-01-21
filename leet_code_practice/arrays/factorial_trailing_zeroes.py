n = 5
def ftz(n):
    if n==0 or n==1:
        return 1
    return n*ftz(n-1)

print(ftz(n))


# optimal method

def trailingZeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
