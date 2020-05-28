# Uses python3
import sys

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#     return a*b


def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b, a % b)


def lcm(a, b):
    """
    lcm takes in two integers and finds the least common multiple using the formula lcm = a / gcd(a, b) * b
    :return: a number representing the least common multiple
    """
    return a // gcd(a, b) * b


if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))

