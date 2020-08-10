def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    assert len(ints) > 0

    min_el = ints[0]
    max_el = ints[0]

    for el in ints:
        if el < min_el:
            min_el = el
        if el > max_el:
            max_el = el

    return (min_el, max_el)

# Tests

print (get_min_max([6, 7, 8, 9, 10, 1, 2, 3, 4]))
# (1, 10)

print (get_min_max([4, 6, 2, 5, 9, 8, -1, 3, 3, 3, 6, 9, 8, 0]))
# (-1, 9)

print (get_min_max([0, 0, 0, 0, 0, 0]))
# (0, 0)

print (get_min_max([-2, -99, -145, -5, -5, -145]))
# (-145, -2)

print (get_min_max([]))
# AssertionError at assert len(ints) > 0

