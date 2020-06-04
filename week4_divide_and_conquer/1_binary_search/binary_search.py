# Uses python3
import sys


def binary_search(lst, tar):
    """
    binary_search function finds the index if a number in a sorted array
    :param lst: sorted array of distinct positive integers in increasing order
    :param tar: integer
    :return: the index of the tar element if it exists in the array, otherwise -1
    """
    left, right = 0, len(lst) - 1
    # write your code here
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == tar:
            return mid
        elif lst[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    data = list(map(int, input().split()[1:]))
    targets = list(map(int, input().split()[1:]))
    for x in targets:
        # print(linear_search(data, x), end=' ')
        print(binary_search(data, x), end=' ')
