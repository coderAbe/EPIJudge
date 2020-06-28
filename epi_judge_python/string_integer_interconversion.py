from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    abs_x = abs(x)
    str_list = []

    while abs_x > 0:
        last_digit = abs_x % 10
        str_list.append(chr(48 + last_digit))
        abs_x //= 10

    result = ''.join(reversed(str_list))

    if x < 0:
        return '-' + result

    return result


def string_to_int(s: str) -> int:
    power_of_10 = 1  
    result = 0 
    char_sign = None
    current_str = s

    if s[0] in '+-':
        char_sign = s[0]
        current_str = s[1:]

    for char in reversed(current_str):
        result += (ord(char) - 48) * power_of_10
        power_of_10 *= 10

    if char_sign == '-':
        return result * -1

    return result

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
