def heapify(arr, n, i):
    left_i = 2 * i + 1
    right_i = 2 * i + 2
    largest_idx = i

    if left_i < n and arr[left_i] > arr[i]:
        largest_idx = left_i
    if right_i < n and arr[right_i] > arr[largest_idx]:
        largest_idx = right_i

    if largest_idx != i:
        arr[i], arr[largest_idx] = arr[largest_idx], arr[i]
        heapify(arr, n, largest_idx)

def heapsort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)

    # Extract the max element one by one and put it at the end, maintaining heap property
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    first = 0
    second = 0
    len_second = len(input_list) // 2
    len_first = len(input_list) - len_second

    heapsort(input_list)

    n1 = len_first - 1
    n2 = len_second - 1
    while True:
        if len(input_list) > 0:
            first += input_list.pop() * (10**n1)
            n1 -= 1
        else:
            break
        if len(input_list) > 0:
            second += input_list.pop() * (10**n2)
            n2 -= 1
        else:
            break

    return [first, second]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[5, 7], [5, 7]])
test_function([[5], [5, 0]])
test_function([[], [0, 0]])
test_function([[4, 6, 2, 5, 9, 8, 1, 3, 3, 3, 6, 9, 8, 0], [9865331, 9864320]])
