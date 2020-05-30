# Uses python3
import sys


def get_change(m):
    """
    get_change finds the minimum number of coins needed to change the input value
    (an integer) into coins with denominations 1, 5, and 10.
    :param m: integer represents the change
    :return: the min number of coins needed to change m
    """
    m1 = m % 10
    m2 = m1 % 5
    return m//10 + m1//5 + m2


if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
