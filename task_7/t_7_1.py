def max_of_two(a, b):
    """
    Compares two values and prints the greater one. If both values are equal, it prints either value.

    :param a: The first value to compare.
    :type a: int | float
    :param b: The second value to compare.
    :type b: int | float
    :return: None
    """
    if a > b:
        print(a)
    else:
        print(b)
max_of_two(1, 2)