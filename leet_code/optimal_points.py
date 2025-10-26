from sys import stdin
from collections import namedtuple


# “Pick minimum points to cover all segments.”

Segment = namedtuple('Segment', 'start end')#[(2,3),(1,4),(3,7)]

def optimal_points(segments):
    points = []
    segments.sort(key=lambda s:s.end)
    while segments:
        point = segments[0].end
        points.append(point)
        segments = [i for i in segments if i.start>point]#if all greater then no value removed

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)


