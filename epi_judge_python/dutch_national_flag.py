import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    lower, equal, bigger = 0, 0, len(A) - 1

    while equal <= bigger:
        if A[equal] < pivot:
            A[lower], A[equal] = A[equal], A[lower]
            lower+=1
            equal+=1
        elif A[equal] > pivot: 
            A[equal], A[bigger] = A[bigger], A[equal]
            bigger-=1
        else: 
            equal+=1



#  def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    #  lower, bigger = 0, len(A) - 1
    #  pivot = A[pivot_index]

    #  while lower < bigger:
        #  if A[lower] <= pivot:
            #  lower += 1
        #  else:
            #  A[lower], A[bigger] = A[bigger], A[lower]
            #  bigger -= 1


    #  if A[bigger] > pivot:
        #  bigger -= 1

    #  lower, equal = 0, bigger 

    #  while lower < equal:
        #  if A[equal] == pivot:
            #  equal -= 1
        #  else:
            #  A[lower], A[equal] = A[equal], A[lower]
            #  lower += 1


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
