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
    prizes = []
    # if n is 0 candies
    if n == 0:
        return prizes
    while n > 0:
        last_prize = prizes[-1] if prizes else 0
        if n <= last_prize:
            prizes[-1] += n
            n = 0
        else:
            new_prize = last_prize + 1
            prizes.append(new_prize)
            n -= new_prize
    return prizes


if __name__ == '__main__':
    n = int(input())
    prizes_l = optimal_summands(n)
    print(len(prizes_l))
    for prize in prizes_l:
        print(prize, end=' ')


