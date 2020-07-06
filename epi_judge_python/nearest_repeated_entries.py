from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    min_distance = len(paragraph)
    words = {}

    for i in range(0, len(paragraph)):
        current_word = paragraph[i] 
        if current_word in words:
            min_distance = min(i - words[current_word], min_distance)
        words[paragraph[i]]  = i

    return min_distance if min_distance != len(paragraph) else -1

 



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
