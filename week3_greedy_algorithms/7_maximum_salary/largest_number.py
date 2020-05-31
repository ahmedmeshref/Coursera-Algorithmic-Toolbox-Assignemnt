# Uses python3


def IsGreaterOrEqual(num, max_num):
    """
    IsGreaterOrEqual takes in two numbers and returns true only if the resulting composition of
    number and max_num in order is greater than or equal to the composition of max_num and num
    """
    return int(str(num) + str(max_num)) >= int(str(num) + str(max_num))


def largest_number(lst):
    """
    largest_number function takes in a list of integers each of any length and composes the largest
    number out of the given inout integers.
    :param lst: list of numbers
    :return: string represents the largest (max) composed number that can be arranged out of all
    given numbers
    """
    answer = ""

    while lst:
        max_number = 0
        for number in lst:
            if IsGreaterOrEqual(number, max_number):
                max_number = number
        answer += str(max_number)
        lst.remove(max_number)

    return answer


if __name__ == "__main__":
    _ = int(input())
    lst = [int(i) for i in input().split()]
    print(largest_number(lst))

