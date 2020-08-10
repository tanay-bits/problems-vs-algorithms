def binary_search(sorted_arr, target, start_idx, end_idx):
    if start_idx == end_idx:
        return (end_idx if sorted_arr[end_idx] == target else -1)

    mid_idx = (start_idx + end_idx) // 2
    mid = sorted_arr[mid_idx]
    if mid == target:
        return mid_idx
    elif mid < target:
        return binary_search(sorted_arr, target, mid_idx + 1, end_idx)
    else:
        return binary_search(sorted_arr, target, start_idx, mid_idx - 1)

def find_rotation_pivot(arr, start_idx, end_idx):
    if start_idx >= end_idx - 1:
        return None

    mid_idx = (start_idx + end_idx) // 2
    left = arr[mid_idx - 1]
    right = arr[mid_idx + 1]
    center = arr[mid_idx]
    start = arr[start_idx]

    if left < center < right:
        if start > center:  # The pivot must be on the left side
            return find_rotation_pivot(arr, start_idx, mid_idx - 1)
        else:               # The pivot must be on the right side
            return find_rotation_pivot(arr, mid_idx + 1, end_idx)
    else:
        if left > center:
            out = mid_idx
        if right < center:
            out = mid_idx + 1
        return out

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    pivot = find_rotation_pivot(input_list, 0, len(input_list) - 1)
    if pivot == None:   # input is already sorted
        sorted_input_list = input_list
        pivot = 0
    else:
        sorted_input_list = input_list[pivot : ] + input_list[ : pivot]
    idx_in_sorted_input = binary_search(sorted_input_list, number, 0, len(input_list) - 1)
    out = (pivot + idx_in_sorted_input) % len(input_list) if idx_in_sorted_input is not -1 else -1
    return out

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Tests:

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass
test_function([[4, 5, 6, 7, 8, 9, 2], 9])
# Pass
test_function([[0, 1, 2, 3, 4, -2], -2])
# Pass
test_function([[4, -2, 0, 1, 2, 3], 0])
# Pass
test_function([[13], 13])
# Pass
test_function([[13], 9])
# Pass
test_function([[], 3])
# Pass

