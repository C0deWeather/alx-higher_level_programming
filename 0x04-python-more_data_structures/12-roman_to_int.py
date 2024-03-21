#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Arguments:
    roman_string (str): thr roman numeral

    Returns:
    int: returns an integer equivalent of the roman numerals
    """
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    r_sum = 0
    i = 0
    try:
        if roman_string is None:
            return 0
        while i < len(roman_string):
            if (i + 1 < len(roman_string) and
                    d[roman_string[i + 1]] > d[roman_string[i]]):
                r_sum += d[roman_string[i + 1]] - d[roman_string[i]]
                i += 2
            else:
                r_sum += d[roman_string[i]]
                i += 1
        return r_sum
    except (TypeError, KeyError):
        return 0
