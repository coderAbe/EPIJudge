from typing import List

from test_framework import generic_test
from collections import namedtuple
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    TupleArray = namedtuple('TupleArray', ['value', 'idx'])
    heap = []
    result = []

    for i in range(0, len(sorted_arrays)):
        heapq.heappush(heap, TupleArray(-sorted_arrays[i].pop(), i))

    while heap:
        curr_smallest = heap[0]
        
        # Check if the current list is empty
        if not sorted_arrays[curr_smallest.idx]:
            next_in_result = heapq.heappop(heap)
            result.append(-next_in_result.value)
        else:
            # Check if next element in list bigger
            next_int = sorted_arrays[curr_smallest.idx].pop()

            if -next_int > curr_smallest.value:
                next_in_result = heapq.heappushpop(heap, TupleArray(-next_int, curr_smallest.idx))
                result.append(-next_in_result.value)
            # if next element is = insert wihout using heap
            else:
                result.append(next_int)

    return  result[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
