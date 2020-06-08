# Uses python3
import math


def diff(p1, p2):
    d1 = (p1[0] - p2[0]) ** 2
    d2 = (p1[1] - p2[1]) ** 2
    return math.sqrt(d1 + d2)


def minimum_distance(n, points):
    # write your code here
    points.sort(key=lambda x: x[0] - x[1])
    print(points)
    min_so_far = 9999999999999
    for i in range(len(points) -1):
        min_so_far = min(min_so_far, diff(points[i], points[i+1]))
    return min_so_far


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    print("{0:.5f}".format(minimum_distance(n, data)))



