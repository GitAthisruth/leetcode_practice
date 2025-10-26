def fibonacci1(n):
    if n<=1:
        return n
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return b

print(fibonacci1(6))


def fibonacci2(n):
    if n<=1:
        return n
    return fibonacci2(n-1)+fibonacci2(n-2)