SEPARATOR = [' ', ',', '.']


def get_int_nearest(index, integers, added_return):
    nearest_integer = 0

    for integer in integers:
        if integer < index and nearest_integer >= (integer - index):
            nearest_integer = integer
    return nearest_integer


def auto_return_v1(string, string_length):
    if not isinstance(string, str):
        return None
    if not isinstance(string_length, int):
        return None

    return string


def auto_return_v2(string, string_length):
    if not isinstance(string, str):
        return None
    if not isinstance(string_length, int):
        return None
    string = [char for char in string]

    len_current_return = 0
    for char_id, char in enumerate(string[:]):
        if char_id + 1 == string_length or ((char_id + 1) % string_length) == 0:
            string.insert(char_id + 1 + len_current_return, '\n')
            len_current_return += 1
    string = ''.join(string)
    return string


def auto_return_v3(string, string_length):
    if not isinstance(string, str):
        return None
    if not isinstance(string_length, int):
        return None
    string = [char for char in string]
    added_return = []
    index_space = [index for index, char in enumerate(string) if char in SEPARATOR]
    for char_id, char in enumerate(string[:]):
        if char_id + 1 == string_length or ((char_id + 1) % string_length) == 0:
            if char_id + 1 not in SEPARATOR:
                return_to_index = get_int_nearest(char_id + 1, index_space, added_return)
                string[return_to_index] = '\n'
                added_return.append(return_to_index)
            else:
                string[char_id + 1] = '\n'
    string = ''.join(string)
    return string
