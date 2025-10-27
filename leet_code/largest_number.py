
def largest_number_naive(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*10, reverse=True)
    numbers = ''.join(numbers)
    return numbers


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))



