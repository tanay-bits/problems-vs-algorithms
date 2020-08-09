def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_el = ints[0]
    max_el = ints[0]

    for el in ints:
        if el < min_el:
            min_el = el
        if el > max_el:
            max_el = el

    return (min_el, max_el)




# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
