from typing import List

from test_framework import generic_test
import bisect

    #  index = bisect.bisect_left(A, k)
    #  if len(A) == index:
        #  return -1

    #  if A[index] != k:
        #  return -1

    #  return index


def search_first_of_k(A: List[int], k: int) -> int:
    lower, upper = 0, len(A) - 1

    result = upper + 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if A[mid] == k:
            if mid > 0 and A[mid-1] == A[mid]:
                upper = mid - 1
            else:
                return mid
        elif A[mid] < k:
            lower = mid + 1;
        else: 
            upper = mid - 1;

    return result if result != len(A) else -1

 
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
