# Uses python3

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


n = int(input())
print(calc_fib(n))
