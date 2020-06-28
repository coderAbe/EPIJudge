from test_framework import generic_test


def square_root(k: int) -> int:

    if not k:
        return 0

    lower, upper = 1, k


    while  lower <= upper:
        current= lower + (upper - lower) // 2
        if current*current > k:
            upper = current - 1
        elif current*current <= k and (current + 1) * (current + 1) > k:
            return current
        else:
           lower = current + 1 
            
    return -1 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
