from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils





def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []

    def find_largest_recur(tree):
        if tree:

            find_largest_recur(tree.right)

            if len(result) == k:
                return

            result.append(tree.data)

            find_largest_recur(tree.left)

    find_largest_recur(tree)


    return result 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
