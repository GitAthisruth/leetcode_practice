def fibonacci_last_digit_of_sum(n):
    n = (n+2) % 60  # Pisano period
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b)%10
        fib = b
    return (fib-1)%10

if __name__ == "__main__":

    n = int(input())
    print(fibonacci_last_digit_of_sum(n))
