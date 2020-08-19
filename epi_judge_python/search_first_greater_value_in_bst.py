from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
import math

def search_for_greater_recursive(node, inpt):
    if not node:
        return None

    left = search_for_greater_recursive(node.left, inpt)
    if left:
        return left
    
    if node.data > inpt:
        return node

    right = search_for_greater_recursive(node.right, inpt)
    if right:
        return right

def search_for_greater(node, inpt):
    root = None 
    curr = node

    while curr:
        if curr.data > inpt:
            root = curr
            curr = curr.left
        else:
            curr = curr.right

    return root 

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    return search_for_greater(tree, k)
    #  return search_for_greater_recursive(tree, k)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
