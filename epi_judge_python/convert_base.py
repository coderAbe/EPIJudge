from test_framework import generic_test
import math
import string


# ASCII 65

def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    if num_as_string == '0':
        return "0"

    is_negative = num_as_string[0] == '-'

    reversed_string = num_as_string[::-1]

    if is_negative:
        reversed_string = reversed_string[0:-1]



    base_10 = 0
    for i in range(len(reversed_string)):
        ascii_value = ord(reversed_string[i])
        num =  ascii_value - (48 if ascii_value < 65 else 55)
        #  num = string.hexdigits.index(reversed_string[i].lower())

        base_10 += num * math.pow(b1, i)

    base_10 = int(base_10)

    result = [] 

    while base_10:
        current_digit = base_10 % b2
        char = str(current_digit) if current_digit < 10 else chr(current_digit+55) 
        #  char = string.hexdigits[current_digit].upper()
        result.append(char)
        base_10 //=b2

    result = "".join(result[::-1])
    if is_negative:
        return '-' + result

    return result
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
