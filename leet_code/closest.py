from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")
    print(list(combinations(points, 2)))
    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))




# def minimum_distance_squared(points):
#     n = len(points)
#     min_val = float("inf")

#     # Compare every pair of points (brute force)
#     for i in range(n-1):
#         for j in range(i + 1, n):
#             x1, y1 = points[i]
#             x2, y2 = points[j]
#             dist_sq = (x1 - x2)**2 + (y1 - y2)**2
#             if dist_sq < min_val:
#                 min_val = dist_sq
#     return min_val


# if __name__ == '__main__':
#     input_n = int(input())
#     points = []
#     for _ in range(input_n):
#         x, y = map(int, input().split())
#         points.append((x, y))  # store as pair

    # print(points)
    # print("{0:.9f}".format(minimum_distance_squared(points)))
