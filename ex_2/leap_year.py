def is_leap_year_v1(year):
    try:
        year = int(year)
    except TypeError:
        return False
    if not isinstance(year, int):
        return False
    return True


def is_leap_year_v2(year):
    try:
        year = int(year)
    except TypeError:
        return False
    if not isinstance(year, int):
        return False
    if (year % 400) == 0:
        return True
    return False


def is_leap_year_v3(year):
    try:
        year = int(year)
    except TypeError:
        return False
    if not isinstance(year, int):
        return False
    if (year % 100) == 0:
        if (year % 400) != 0:
            return False
    if (year % 400) == 0:
        return True
    return False


def is_leap_year_v4(year):
    try:
        year = int(year)
    except TypeError:
        return False
    if not isinstance(year, int):
        return False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
    return False
