import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    i, j = 0, len(s) - 1
    while i <= j: 
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    l, m = 0, 0

    while l <= len(s) - 1:
        while l < len(s) - 1 and s[l] == " ":
            l += 1
        m = l
        while m < len(s) -1 and s[m + 1] != " ":
            m += 1

        new_end = m + 1
        while l < m:
            new_temp = s[l]
            s[l] = s[m]
            s[m] = new_temp
            l += 1
            m -= 1
            
        l, m = new_end, new_end

        

    return s
            
        


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
