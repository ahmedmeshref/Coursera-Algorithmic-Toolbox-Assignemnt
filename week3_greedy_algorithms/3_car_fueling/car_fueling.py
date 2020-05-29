# python3
import sys


def compute_min_refills(distance, tank, stops):
    """
    compute_min_refills finds the min refills needed for a car to travel a distance from a to b
    :param distance: distance between two points a, and b
    :param tank: max distance you can travel on a full tank
    :param stops: a list of integer, each represents a gas station position on the road
    :return: number of the min refills possible to reach the target city, if it is impossible return -1
    """
    current_pos = 0
    min_refills = 0
    current_stop = 0
    while current_pos + tank < distance:
        furthest_stop = False
        while current_stop < len(stops) and current_pos + tank >= stops[current_stop]:
            furthest_stop = stops[current_stop]
            current_stop += 1
        # if no furthest_stop can be reached, then it is impossible to reach b
        if not furthest_stop:
            return -1
        current_pos = furthest_stop
        min_refills += 1
    return min_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))


