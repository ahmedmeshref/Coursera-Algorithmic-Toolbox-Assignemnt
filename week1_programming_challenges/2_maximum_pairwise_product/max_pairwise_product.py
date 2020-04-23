"""
Given a list of number find the highest product between two of its elements.
Ex: l = [1, 2, 6, 3, 4]
ans: 24
"""
# import random for creating a stress test
import random


# def max_pairwise_product(numbers):
#     """
#     brute force solution: getting every pair of elements and storing the highest
#     TimeComplexity: O(n^2)
#     """
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product, numbers[first] * numbers[second])
#     return max_product


def max_pairwise_product(numbers):
    """
    max_pairwise_product gets the two biggest numbers and returns the product of them
    TimeComplexity: O(n)
    """
    biggest = -9999999999999
    second_bigest = -9999999999999
    for ele in numbers:
        if ele > biggest:
            biggest, second_bigest = ele, biggest
        elif ele > second_bigest:
            second_bigest = ele
    return biggest * second_bigest


# # building a stress test to help in validating the answer of my optimized algrithm by compare the output
# # to the brute force output
# def stress_test():
#     while True:
#         rand_nums = random.sample(range(0, 2000), 1000)
#         print(rand_nums)
#         ans = max_pairwise_product(rand_nums)
#         ans_2 = max_pairwise_product(rand_nums)
#         if ans == ans_2:
#             print("OK")
#         else:
#             return f"Wrong Answer \nOptimized alg ans: {ans} \nBrute Force ans: {ans_2}"
# print(stress_test())


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

