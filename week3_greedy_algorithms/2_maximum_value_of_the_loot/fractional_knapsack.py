
def get_optimal_value(capacity, items):
    """
    get_optimal_value function implements an algorithm for the fractional knapsack problem
    :param capacity: Number represents the total capacity of the bag
    :param items: list of list that contains values and weights of each item, where items[𝑖] = [value(𝑖), weight(𝑖)]
    :return: decimal number represents the maximal value of fractions of items that fit into the bag of weight capacity.
    """
    out = 0
    # sort all items by their price_per_unit
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    for v, w in items:
        can_fit = capacity - w
        # if the element can fit into the bag, take the whole item.
        if can_fit >= 0:
            out += v
            capacity = can_fit
        # otherwise, take as much of the item's weight as possible (price_per_unit * capacity).
        else:
            out += (v/w) * capacity
            return out
    return out


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    items = []
    for i in range(n):
        items.append(list(map(int, input().split())))
    opt_value = get_optimal_value(capacity, items)
    print("{:.10f}".format(opt_value))


