from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    a, b = m - 1, n - 1     

    next_slot = len(A) - 1

    while a >= 0 or b >= 0: 
        if a < 0:
            A[next_slot] = B[b]
            b -= 1
        elif b < 0:
            return A
        elif A[a] < B[b]:
            A[next_slot] = B[b]
            b -= 1
        else:
            A[next_slot] = A[a]
            a -= 1
        next_slot -= 1


    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
