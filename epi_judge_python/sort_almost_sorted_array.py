from typing import Iterator, List

from test_framework import generic_test

import heapq 


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    h = [] 
    result = []

    seq = iter(sequence)

    # insert k elements to heap
    for i in range(k):
        heapq.heappush(h, next(seq))

    # start retrieving and pushing elements one by one while assigning to sorted sequence
    for next_seq in sequence:
        heapq.heappush(h, next_seq)
        result.append(heapq.heappop(h))

    result.extend(heapq.nsmallest(k, h))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
