def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    n = len(input_list)
    if n == 0:
        return []
    left_next = 0
    right_next = n - 1
    i = 0
    while i <= right_next:
        cur = input_list[i]
        if cur == 0:
            input_list[i], input_list[left_next] = input_list[left_next], input_list[i]
            left_next += 1
            i += 1
        elif cur == 1:
            i += 1
        elif cur == 2:
            input_list[i], input_list[right_next] = input_list[right_next], input_list[i]
            right_next -= 1
        else:
            print("Invalid input!")
            return None

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Tests:

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Pass
test_function([0, 0, 0, 0, 0, 0])
# Pass
test_function([2])
# Pass
test_function([])
# Pass
