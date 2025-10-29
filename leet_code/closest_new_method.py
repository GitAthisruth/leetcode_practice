from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance_squared(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def closest_pair(points_sorted_by_x):
    n = len(points_sorted_by_x)
    if n <= 3:
        # Brute force for small subsets
        return min(
            (distance_squared(points_sorted_by_x[i], points_sorted_by_x[j])
             for i in range(n) for j in range(i + 1, n)),
            default=float("inf")
        )

    mid = n // 2
    mid_x = points_sorted_by_x[mid].x

    # Divide
    d_left = closest_pair(points_sorted_by_x[:mid])
    d_right = closest_pair(points_sorted_by_x[mid:])
    d = min(d_left, d_right)

    # Merge step: consider points near dividing line
    strip = [p for p in points_sorted_by_x if abs(p.x - mid_x) < sqrt(d)]
    strip.sort(key=lambda p: p.y)

    # Check each point with up to 7 next points in y-sorted strip
    min_strip = d
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j].y - strip[i].y)**2 >= min_strip:
                break
            min_strip = min(min_strip, distance_squared(strip[i], strip[j]))

    return min(d, min_strip)

if __name__ == '__main__':
    n = int(input())
    points = [Point(*map(int, input().split())) for _ in range(n)]
    points.sort(key=lambda p: p.x)
    result = sqrt(closest_pair(points))
    print("{0:.9f}".format(result))
