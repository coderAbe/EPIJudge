from typing import Set

from test_framework import generic_test
import collections
import string

def shortest_path_BFS(D,s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    queue = collections.deque([StringWithDistance(s,0)])
    D.remove(s)
    visited = set()

    while queue:
        current = queue.popleft()
        if current.candidate_string ==  t:
            return current.distance 
        for i in range(len(current.candidate_string)):
            for c in string.ascii_lowercase:
                cand = current.candidate_string[:i] + c + current.candidate_string[i+1:]
                if cand in D:
                    #  candidate_string : [ variant1, variant2, variant3]
                    queue.append(StringWithDistance(cand,current.distance +1))
                    D.remove(cand)

    return -1

def transform_string(D: Set[str], s: str, t: str) -> int:
    return shortest_path_BFS(D, s, t)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
