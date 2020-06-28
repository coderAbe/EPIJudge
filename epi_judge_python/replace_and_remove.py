import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    number_of_b = 0
    number_of_a = 0
    new_size = size

    for i in range(size):
        # Trucazo count a
        if s[i] == 'a':
            number_of_a += 1
        # Trucazo count b
        if s[i] == 'b':
            s[i] = ''
            number_of_b += 1
            # Update size
        # move element index - b
        elif number_of_b > 0:
            s[i - number_of_b] = s[i]
            s[i] = ''

    new_size -= number_of_b
    j = new_size - 1
    new_size += number_of_a

    # trucazo similar a b pero buscando anadir a
    while number_of_a > 0:
        if s[j] == 'a':
            s[j + number_of_a] = 'd'
            s[j + number_of_a - 1] = 'd'
            number_of_a -= 1
        elif s[j] != '':
            s[j + number_of_a], s[j] = s[j], s[j + number_of_a]
        j-=1
       
    return new_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
