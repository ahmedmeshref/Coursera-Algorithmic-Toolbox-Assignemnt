# Uses python3
import sys


def optimal_summands(n):
    """
    optimal_summands function takes in a positive integer 𝑛 and represents it as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
    𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
    :param n: positive integer
    :return: two lines, the first represents the number of pairwise distinct positive integers,
    the second represents all the output distinct integers
    """
    summands = []
    # if n is 0 candies
    if n == 0:
        return summands
    while n > 0:
        last_prize = summands[-1] if summands else 0
        if n <= last_prize:
            summands[-1] += n
            return summands
        else:
            new_prize = last_prize + 1
            summands.append(new_prize)
            n -= new_prize
    return summands


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
