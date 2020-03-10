"""
Finds how many distinct powers generated by a^b given the range  2 ≤ a ≤ n and 2 ≤ b ≤ n
where n is a positive integer
"""


def distinct_powers(a, b):
    """
    Finds and returns the number of distinct powers of a and b

    Example:
    >>> distinct_powers(5, 5)
    15

    :param a: Limit of a
    :type a int
    :param b: limit of b
    :type b int
    :return: number of distinct powers
    :rtype: int
    """

    # sanity checks
    if a is None or b is None:
        raise ValueError("Expected a or b to be an integer")

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Expected a or b to be a integer")

    powers = set(m ** n for m in range(2, a + 1) for n in range(2, b + 1))

    return len(powers)


if __name__ == "__main__":
    x = 100
    y = 100
    no_of_distinct_powers = distinct_powers(x, y)
    print(f"Distinct powers given a={x} and b ={y} is {no_of_distinct_powers}")