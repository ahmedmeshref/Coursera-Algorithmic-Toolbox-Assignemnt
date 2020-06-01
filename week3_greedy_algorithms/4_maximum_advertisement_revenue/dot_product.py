# Uses python3


def max_ads_revenue(a, b):
    """
    max_ads_revenue function distribute the ads profite given in a list a among the slots given in b to
     maximize the total revenue.
    :param a: list of integers, where a𝑖 represents the profit per click of the 𝑖-th ad
    :param b: list of integers, where b𝑖 is the average number of clicks per day of the 𝑖-th slot
    :return: an integer represents the max profit possible of placing the ads on the website
    """
    # sort a, b
    a.sort()
    b.sort()
    return sum([ad*click for ad, click in zip(a, b)])


if __name__ == '__main__':
    _ = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_ads_revenue(a, b))
