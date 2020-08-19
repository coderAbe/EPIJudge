import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    start, current, end = 0, 0, len(A) - 1

    while current <= end:
        if A[current] < pivot:
            A[start], A[current] = A[current], A[start]
            start+=1
            current+=1
        elif A[current] > pivot: 
            A[current], A[end] = A[end], A[current]
            end-=1
        else: 
            current+=1



#  def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    #  start, end = 0, len(A) - 1
    #  pivot = A[pivot_index]

    #  while start < end:
        #  if A[start] <= pivot:
            #  start += 1
        #  else:
            #  A[start], A[end] = A[end], A[start]
            #  end -= 1


    #  if A[end] > pivot:
        #  end -= 1

    #  start, current = 0, end 

    #  while start < current:
        #  if A[current] == pivot:
            #  current -= 1
        #  else:
            #  A[start], A[current] = A[current], A[start]
            #  start += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
