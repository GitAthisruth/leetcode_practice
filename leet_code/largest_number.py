
def largest_number_naive(numbers):

    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x:x*10, reverse=True)
    print(numbers)
    numbers = ''.join(numbers)
    return numbers


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))



print("9999999999">"1111111111")