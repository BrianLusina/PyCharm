def flatten(linked_array):
    m = []
    for x in linked_array:
        if is_iterable(x) and not isinstance(x, (str, bytes)):
            m += flatten(x)
        elif x is not None:
            m.append(x)
    return m


def is_iterable(val):
    try:
        iter(val)
    except TypeError:
        return False
    else:
        return True
