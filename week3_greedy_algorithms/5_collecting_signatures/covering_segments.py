# Uses python3
import sys


def optimal_points(segments, n):
    """
    optimal_points function takes in a set of segments and it marks as few points on a line as possible
    so that each segment contains at least one marked point.
    :param segments: a list of points on a line. Ex: [[x1, y1], [x2, y2]]
    :param n: number of segments
    :return: a list with all of the touched points in the line
    """
    segments.sort(key=lambda x: x[1])

    coordinates = []
    index = 0
    while index < n:
        cur_point = segments[index]
        while index < n - 1 and cur_point[1] >= segments[index+1][0]:
            index += 1
        coordinates.append(cur_point[1])
        index += 1
    return coordinates


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    lst = []
    for _ in range(n):
        p = [int(n) for n in input().split()]
        lst.append(p)
    points = optimal_points(lst, n)
    print(len(points))
    print(*points)
