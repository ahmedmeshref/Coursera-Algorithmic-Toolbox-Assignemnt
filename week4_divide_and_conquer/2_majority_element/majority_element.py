"""
Task: The goal in this code problem is to check whether an input sequence contains a majority element.

Input Format: The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints. 1 ≤ 𝑛 ≤ 105
; 0 ≤ 𝑎𝑖 ≤ 109
for all 0 ≤ 𝑖 < 𝑛.

Output Format: Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
and 0 otherwise.
"""

from collections import Counter


# O(n) solution
def get_maj_element(nums, len_nums):
    """
    get_maj_element check whether an input sequence contains a majority element which appeared more than len_of_nums/2
    :param nums: list of integer
    :param len_nums: integer represents the number of elements in nums
    :return: 1 if a majority element exists, 0 otherwise
    """
    counts = Counter(nums)
    for ele in counts:
        if counts[ele] > len_nums / 2:
            return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    # get_maj_element O(n) solution
    print(get_maj_element(lst, n))
