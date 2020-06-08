# Uses python3
import sys


def inner_merge(left, right):
    global no_inversions
    res = []
    l_pointer = r_pointer = 0
    while l_pointer < len(left) and r_pointer < len(right):
        if left[l_pointer] > right[r_pointer]:
            res.append(right[r_pointer])
            r_pointer += 1
            no_inversions += len(left) - l_pointer
        else:
            res.append(left[l_pointer])
            l_pointer += 1
    res.extend(left[l_pointer:])
    res.extend(right[r_pointer:])
    return res


def merge_sort(arr):
    """
    merge sort function sorts the array elements and counts the number of inversions of a given sequence.
    :param arr: Array of unsorted integers
    :return: Array of sorted elements in arr
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return inner_merge(left, right)


if __name__ == '__main__':
    no_inversions = 0
    _ = int(input())
    lst = list(map(int, input().split()))
    merge_sort(lst)
    print(no_inversions)
