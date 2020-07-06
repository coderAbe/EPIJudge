from test_framework import generic_test

import collections 

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:

    magazine_dict = collections.defaultdict(int)

    for char in magazine_text:
        magazine_dict[char] += 1

    for char in letter_text:
        if not magazine_dict[char]:
            return False
        else:
            magazine_dict[char] -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
