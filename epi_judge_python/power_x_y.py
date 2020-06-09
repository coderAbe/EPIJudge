from test_framework import generic_test
import math

def power(x: float, y: int) -> float:
    result = 1

    power_of_2 = math.floor(abs(y/2))

    is_odd = y % 2 > 0

    for _ in range(power_of_2):
        result *= x * x

    if is_odd:
        result *= x

    if y < 0: 
        return 1/result

    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
