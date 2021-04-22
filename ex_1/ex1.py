def join(elements, separator):
    joined_string = ''
    len_elements = len(elements)

    if not isinstance(elements, list):
        return None
    if not isinstance(separator, str):
        return None

    for index, element in enumerate(elements):
        if index + 1 == len_elements:
            joined_string += element
        else:
            joined_string += element + separator
    return joined_string


def average(integers):
    to_ret = 0
    if not isinstance(integers, list):
        return None

    if len(integers) == 0:
        return 0

    for integer in integers:
        if not isinstance(integer, int):
            return None
        to_ret += integer
    if to_ret == 0:
        return to_ret
    return to_ret / len(integers)
