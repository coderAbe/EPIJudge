from test_framework import generic_test

import functools 

@functools.lru_cache(None)
def levenshtein_distance(A: str, B: str) -> int:
    
    if not len(A) and len(B):
        return len(B)
    if not len(B) and len(A):
        return len(A)

    if not len(A) and not len(B):
        return 0

    if A[-1] == B[-1]:
        return levenshtein_distance(A[:-1], B[:-1])
    
    return 1 + min(
            levenshtein_distance(A[:-1], B[:-1]), # edit
            levenshtein_distance(A[:-1], B), # delete
            levenshtein_distance(A, B[:-1]), # insert
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
