def sqrtHelper(arr, start, end, number):
    if start >= end:
        cur = arr[start]
        if cur * cur == number:
            return cur
        else:
            return arr[start - 1]

    mid = (start + end) // 2
    cur = arr[mid]
    curSq = cur * cur
    if curSq == number:
        return cur
    elif curSq > number:
        return sqrtHelper(arr, start, mid, number)
    else:
        return sqrtHelper(arr, mid + 1, end, number)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert number >= 0
    candidates = [x for x in range(number + 1)]
    return sqrtHelper(candidates, 0, len(candidates) - 1, number)

# Tests:

print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Pass
print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Pass
print ("Pass" if  (10000 == sqrt(100000001)) else "Fail")
# Pass
