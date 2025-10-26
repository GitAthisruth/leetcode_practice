def fibonacci_last_digit(n):
    n = n % 60  # Pisano period
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b)%10 
    return (b*(a+b)%10)%10
 

n = int(input())
last_digit_sum = (fibonacci_last_digit(n))
print(last_digit_sum)


# F0**2​+F1**2​+⋯+Fn**2​=Fn​*Fn+1​