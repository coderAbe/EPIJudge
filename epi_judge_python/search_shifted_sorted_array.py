from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    start, end = 0, len(A) - 1

    while end - start > 1:
        mid = (start + end) // 2
        if A[start] > A[end]:
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid
        if A[start] < A[mid]:
            return start

    return end if A[start] > A[end]else start


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
