# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#     sum = 1
#
#     for _ in range(n - 1):
#         previous, current = current, (previous + current)%10
#         sum += current
#
#     return sum % 10


memo = {}


def calc_fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    else:
        f = calc_fib(n - 1) + calc_fib(n - 2)
    memo[n] = f
    return f


def fibonacci_sum(n):
    # sum of fib f(1) + f(2) + ... + f(n) = fib(n + 2) - 1
    if n < 2:
        return n
    return (calc_fib(n + 2) - 1) % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum(n))
