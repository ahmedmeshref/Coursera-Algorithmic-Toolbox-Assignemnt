# Uses python3
import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)% m

    return current


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n, m))
