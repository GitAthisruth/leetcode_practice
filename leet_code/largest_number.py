from itertools import permutations


def largest_number_naive(numbers):

    numbers = list(map(int, numbers))
    numbers.sort(reverse=True)
    numbers = int(''.join(map(str, numbers)))
    return numbers


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))



