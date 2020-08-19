from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    
    a, b = 0, 0
    result = []

    while a < len(A) and b < len(B): 
        currA = A[a]
        currB = B[b]
        # If currA == currB add it to the result, then advance the idx until diff value
        if currA == currB:
            result.append(currA)
            # Advance a index until diff value
            while a < len(A) and currA == A[a]:
                a += 1
            # Advance b index until diff value
            while b < len(B) and currB == B[b]:
                b += 1
        # Get rid of minor value by advancing the idx (the arrays are sorted so the minor value is not present on the other array)
        elif currA < currB:
            a += 1
        else:
            b += 1

    return result 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
