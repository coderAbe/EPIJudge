from typing import List

from test_framework import generic_test, test_utils

import collections
import functools 

def string_hash(s):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    id = 1
    for char in s:
        id *= 
    return count_dict 


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    strings = collections.defaultdict(list)
     
    for s in dictionary: 
        strings[string_hash(s)].append(s)

    return [ group for group in strings.values() if len(group) >= 2 ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
