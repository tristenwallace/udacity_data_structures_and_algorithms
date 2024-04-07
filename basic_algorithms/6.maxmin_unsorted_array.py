def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:  # Check for empty list
        return (None, None)

    min_val = max_val = ints[0]  # Initialize min and max with the first element

    for num in ints[1:]:  # Start iterating from the second element
        if num < min_val:
            min_val = num  # Update min
        elif num > max_val:
            max_val = num  # Update max

    return (min_val, max_val)

# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")