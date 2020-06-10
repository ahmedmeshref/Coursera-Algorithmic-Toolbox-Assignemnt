# Uses python3
import sys
import random


def swap_left(arr, start, high):
    i = start
    j = high
    while i < j:
        if arr[i] == arr[j]:
            arr[i], arr[j - 1] = arr[j - 1], arr[i]
            j -= 1
        i += 1
    return j


def swap_right(arr, start, high):
    i = start
    j = high
    while i < j:
        if arr[i] == arr[j]:
            arr[i + 1], arr[j] = arr[j], arr[i + 1]
            i += 1
        j -= 1
    return i


def partition3(array, start, end):
    pivot = array[start]
    # low tracks elements greater than pivot
    low = start + 1
    # high tracks elements less than pivot
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    m1, m2 = swap_left(array, start, high), swap_right(array, high, end)
    return m1, m2


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1)
    randomized_quick_sort(a, m2+1, r)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    randomized_quick_sort(lst, 0, n - 1)
    for x in lst:
        print(x, end=' ')
