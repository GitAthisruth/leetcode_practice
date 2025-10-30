from sys import stdin

import bisect #module used to find in which index a number will place.

def points_cover(start,end,points):
    start.sort()
    end.sort()
    count = []
    for p in points:
        right_bisect = bisect.bisect_right(start,p)
        left_bisect = bisect.bisect_left(end,p)
        count.append(right_bisect-left_bisect)

    return count




if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
