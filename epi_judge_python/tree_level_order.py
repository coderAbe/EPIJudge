from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

    if not tree:
        return []

    parents = deque()
    childs = deque()
    result = []

    parents.append(tree)

    level = []
    while parents:
        current = parents.popleft()
        level.append(current.data)

        if current.left:
            childs.append(current.left) 
        if current.right:
            childs.append(current.right)

        if not parents:
            result.append(level)
            level = []
            parents,  childs = childs, parents
        
    return result 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
