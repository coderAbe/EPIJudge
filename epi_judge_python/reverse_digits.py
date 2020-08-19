from test_framework import generic_test
import math

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    result, result_power = 0, 0
    curr = abs(x)
    power = math.floor(math.log10(curr))

    while curr > 0 and power >= 0 :
        result += math.floor((curr // math.pow(10, power)) * math.pow(10, result_power))
        curr %=  math.floor(math.pow(10, power))
        result_power += 1
        power -= 1


    return result * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
